t = int(input())

for j in range(t):

    n = int(input())
    s = input()

    flag = 0

    if s[-1] == '0' and s[-2] == '2' and s[-3] == '0' and s[-4] == '2':
        flag = flag + 1

    elif s[0] == '2' and s[-1] == '0' and s[-2] == '2' and s[-3] == '0':
        flag = flag + 1

    elif s[0] == '2' and s[1] == '0' and s[2] == '2' and s[-1] == '0':
        flag = flag + 1
    elif s[0] == '2' and s[1] == '0' and s[-2] == '2' and s[-1] == '0':
        flag = flag + 1

    elif s[0] == '2' and s[1] == '0' and s[2] == '2' and s[3] == '0':
        flag = flag + 1

    if flag == 0:
        print("NO")
    else:
        print("YES")
