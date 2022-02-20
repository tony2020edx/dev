t = int(input())



for j in range(t):

    x, y = map(int, input().split())
    s = input()

    x_dir , y_dir = 0, 0

    for i in range(len(s)):

        if s[i] == 'R' and x >0:
            x_dir += 1
        elif s[i] == 'L' and x <0:
            x_dir -= 1
        elif s[i] == 'U' and y >0:
            y_dir += 1
        elif s[i] == 'D' and y <0:
            y_dir -= 1

    if abs(x_dir) >= abs(x) and abs(y_dir) >= abs(y):
        print("YES")
    else:
        print("NO")



