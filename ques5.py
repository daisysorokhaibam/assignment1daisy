# Q5. Write a program that takes a string input from the user and writes it to a text file.

str1 = input("What would you like to say to the audience: ")
file_object = open(r"C:/Users/daisy/OneDrive/Documents/python and ml internship/ques5.txt","w")
print(str1, file = file_object)