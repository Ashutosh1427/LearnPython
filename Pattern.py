for i in range(3):
    for j in range(3):
        print('$',end=' ')
    print(end='\n')
###############################
for i in range(3):
    for j in range(i+1):
        print('$',end=' ')
    print(end='\n')

##############################
for i in range(3):
    for j in range(3-i):
        print('$',end=' ')
    print(end='\n')
