devices=["R1","R2","R3","S1","S2"]
for item in devices:
    print(item)

switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)

print(switches)
