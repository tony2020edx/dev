alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

n, q = map(int, input().split())

s = input()

val = []

for i in s:
    val.append(alphabets.index(i)+1)

for j in range(q):

    l, r = map(int, input().split())

    count = sum(val[l-1:r])
    print(count)











