devices=[]
file = open("devices.txt","r")
for item in file:
    item = item.strip()
    devices.append(item)
#    print(item)
file.close()
print(devices)
