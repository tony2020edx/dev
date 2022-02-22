t = int(input())

for i in range(t):

    n = int(input())
    s = input()

    flag = 0

    if s[0:4] == '2020' or s[-4:] == '2020':
        flag = flag + 1

    if s[0] == '2' and s[-3] == '0' and s[-2] == '2' and s[-1] == '0':
        flag = flag + 1

    if s[0] == '2' and s[1] == '0' and s[-2] == '2' and s[-1] == '0':
        flag = flag + 1

    if s[0] == '2' and s[1] == '0' and s[2] == '2' and s[-1] == '0':
        flag = flag + 1

    if flag == 0:
        print("NO")
    else:
        print("YES")
