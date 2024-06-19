# Q19. Write a python program that removes all punctuation from a given string.

import string
str1 = "Hii!! How are you doing?"
print("The original string is : ", str1)
for punctuation in string.punctuation:
    str1 = str1.replace(punctuation, '')
print("The string after punctuation filter : " + str1)