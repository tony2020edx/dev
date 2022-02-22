text = ['aa', 'aba', 'aca', 'abca', 'acba', 'abbacca', 'accabba']

t = int(input())

for k in range(t):
    n = int(input())
    string = input()

    flag = True

    for i in text:
        if string.count(i) > 0:
            print(len(i))
            flag = False
            break

    if flag:
        print(-1)




