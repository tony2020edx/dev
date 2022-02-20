str = input()

n = len(str)

count = 0

for i in range(n//2):

    if str[i] != str[n-i-1]:

        count = count + 1
    else:
        pass


if (n%2 == 0):

    if count == 1:
        print("YES")
    else:
        print("NO")
else:
    if count <=1:
        print("YES")
    else:
        print("NO")