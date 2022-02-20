#codeforces 1 1504A Python Solution

def palindrome(user_input):
    if user_input == user_input[::-1]:
        return True
    else:
        return False


t = int(input())

for j in range(t):
    ui = input()

    all_a_flag = False

    if ui.count('a') == len(ui):
        print("NO")
    else:
        if palindrome(ui + 'a'):
            print('YES')
            print('a' + ui)

        else:
            print('YES')
            print(ui + 'a')
