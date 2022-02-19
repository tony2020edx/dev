alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

n, q = map(int, input().split())

s = input()

for i in range(q):

    l, r = map(int, input().split())

    sub_segment = s[l - 1:r] #gnerate sub sequence

    result = 0

    for j in sub_segment:
        data = alphabets.index(j) + 1 # get the indext of the value based on the alphabet and add one , because indexing starts at zero
        result += data

    print(result)
