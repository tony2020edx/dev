# dominant character - https://codeforces.com/contest/1605/problem/C

def smallest_substring(text):
    res = []

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            if len(text[i:j]) >= 2 and text[i:j].count('a') > text[i:j].count('b') and text[i:j].count('a') > text[i:j].count('c'):
                res.append(text[i:j])

    if len(res) != 0:
        return min(res)

    else:
        return -1



t = int(input())

for k in range(t):
    n = int(input())
    string = input()

    print(smallest_substring(string))
