a=20
b=10
print(a+b) #Addition-Both operands can be either number or strings
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #floating point division
print(a//b) #floor division-may return as int or float but always floor value of the final result
print(a%b)
print(a**b)
"""
+ 
    -> It works as arithemetic operator when both the operands are numbers but when both the operands are strings, it will behave as concat operator
    -> It throws TypeError when one operand is number and other is string
"""
print('10'+'20')
#print('10'+20) #TypeError

"""
*
    -> It works as multiplication operator when both the operands are numbers but when one is string and other is integer then it beahves as string repeatation operator
    -> It throws TypeError when both operands are string
"""
print('hello'*2)
#print('hello'*'world') #TypeError