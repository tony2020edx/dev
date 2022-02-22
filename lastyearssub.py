
def generate_sub(s,length):
    for i in range(len(s) - length + 1):
        yield s[i:i+length]


t = int(input())

for i in range(t):

    n = int(input())
    string = input()

    p = list(generate_sub(string, n))
    #print(p)

    res = []

    for i in range(len(p)):
        res.append(p[i][i])

    print(''.join(res))







