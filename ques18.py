# Q18. Write a python program that checks if two strings are anagrams of each other.

def check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
s1 = "heart"
s2 = "earth"
check(s1, s2)