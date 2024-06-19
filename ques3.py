# Q3. Write a python program that calculates the factorial of a given number.

num = int(input("Enter the number whose factorial you want to calculate: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)
