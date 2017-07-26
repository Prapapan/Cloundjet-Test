for i in range(30,301):
    if i%7==0 and i%13==0:
        print('abcdefghijklmnopqrstuvwxyz')
    elif i%7==0 :
        print('abc')
    elif i%13==0 :
        print('xyz')
    else:
        print(i)
    
