# Check even/odd
if int(input('enter any integer'))%2==0:
    print('Even')
else:
    print('Odd')

# Check leap/non leap year
if int(input('enter any year'))%400==0:
    print('Leap Year')
elif int(input('enter any year'))%4==0 and int(input('enter any year'))%100!=0:
    print('Leap Year')
else:
    print('Not a Leap Year')