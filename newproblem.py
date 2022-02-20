

#function to shitf the character in the string to the right by n

def shift(string, n):
    return string[n:] + string[:n]

print(shift("abc", 1))
