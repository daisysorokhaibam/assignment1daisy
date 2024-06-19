# Q25. Write a program that copies the contents of one text file to another.

with open("C:/Users/daisy/OneDrive/Documents/python and ml internship/first file.txt", "r") as firstfile, open("C:/Users/daisy/OneDrive/Documents/python and ml internship/second file.txt", "a") as secondfile:
    for line in firstfile:
        secondfile.write(line)