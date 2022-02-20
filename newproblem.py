
#function to create take a string as input, then return a string in a way that the first element is added once, the second twice and so on.

s = input("Enter a string: ")

def con(s):
    new = ""
    for i in range(len(s)):
        new += s[i] * (i+1)
    return new

print(con(s))