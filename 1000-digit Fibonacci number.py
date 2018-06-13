Number = 1
Store = 0
Last = 0
index = 1

print('1 1')

while(True):
    index += 1
    Store = Number
    Number = Number + Last
    Last = Store
    print(str(index)+ ' ' + str(Number))
    if len(str(Number)) == 1000:
        break
