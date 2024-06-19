# Q11. Write a python program that generates the first n numbers in the Fibonacci sequence.

n = int(input("Enter how many terms to generate: "))
f = [0,1]
for i in range(2,n):
    nn = f[-1]+f[-2]
    f.append(nn)
print("The Fibonacci Series for given number is: ", nn)