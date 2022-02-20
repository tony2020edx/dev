t = int(input())

for j in range(t):
    px, py = map(int, input().split())
    s = input()
    R_count = s.count('R')
    U_count = s.count('U')
    D_count = s.count('D')
    L_count = s.count('L')

    flag = 0

    if px >= 0 and py >= 0:
        if U_count >= py and R_count >= px:
            flag = 1
    elif px < 0 and py >= 0:
        if U_count >= py and L_count >= abs(px):
            flag = 1
    elif px < 0 and py < 0:
        if L_count >= abs(px) and D_count >= abs(py):
            flag = 1
    elif px >= 0 and py < 0:
        if R_count >= px and D_count >= abs(py):
            flag = 1

    if flag == 0:
        print('NO')
    else:
        print('YES')

