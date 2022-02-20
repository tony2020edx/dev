
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

t = int(input())

for j in range(t):
    st = input()

    for i in reversed(range(len(st))):

        if st[0] == alphabets[i]:
            st = st.replace(st[0], "", 1)
        elif st[-1] == alphabets[i]:
            st = st.replace(st[-1], "", 1)
        else:
            print("NO")
            break

        if len(st) == 0:
            print("YES")
            break

