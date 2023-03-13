# Question 22

# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

s = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
l = s.split(" ")
freq = {}


def count_occurences(arr):
    for word in arr:
        if l.count(word):
            isKeyPresent = word in freq
            if isKeyPresent:
                freq[word] += 1
            else:
                freq[word] = 1


count_occurences(l)
sorted_freq = sorted(freq.items(), key=lambda item: item[0])
print(dict(sorted_freq))
