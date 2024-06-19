# Q16. Write a program in python that counts the frequency of each character in a string.

test_str = "DaisyLovesCakes"

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))