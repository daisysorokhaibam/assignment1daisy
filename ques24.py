# Q24. Write a program that acts as a simple calculator. It should take two
# numbers and an operator (+, -, *, /) as input and print the result.

a=int(input('enter first number: '))
operand=input('enter operation: ')
b=int(input('enter second number: '))
if(operand=='+'):
    print(a+b)
elif(operand=='-'):
    print(a-b)
elif(operand=='/'):
    print(a/b)
elif(operand=='*'):
    print(a*b)
else:
    print('enter valid operation: ')