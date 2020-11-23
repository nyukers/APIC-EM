aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is good IPv4 ACL.")
elif aclNum >= 100 and aclNum <= 199:
    print("This is extended IPv4 ACL.")
else:
    print("This is not good  or ext IPv4 ACL.")
