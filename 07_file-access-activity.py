file = open("devices2.txt","a")

while True:
    NewItem = input('Enter new device name: ')
    if NewItem == 'quit':
        print('All done!')
        break
    
    NewItem = NewItem.strip()
    file.write(NewItem+"\n")
    print(NewItem)
    
file.close()

