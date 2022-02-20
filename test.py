def palindrome(user_input):
    if user_input == user_input[::-1]:
        return True
    else:
        return False


t = int(input())

for j in range(t):
    ui = list(input())

    list_input = []
    not_palindrome = []

    for i in range(len(ui) + 1):
        first = ui[0:i]
        second = ui[i:]

        first.append('a')
        final = first + second

        list_input.append("".join(final))

        for k in range(len(list_input)):
            if palindrome(list_input[k]):
                break
            else:
                not_palindrome.append(list_input[k])

    if len(not_palindrome) == 0:
        print("NO")

    else:
        print("YES")
        print(not_palindrome[0])
