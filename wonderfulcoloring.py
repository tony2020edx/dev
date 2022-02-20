t = int(input())

for i in range(t):
    s = input()
    checked = []
    single = []
    double = []

    for j in range(len(s)):

        if s[j] not in checked:
            checked.append(s[j])
            if s.count(s[j]) == 1:
                single.append(s[j])
            elif s.count(s[j]) >= 2:
                double.append(s[j])

    single_length = len(single)
    double_length = len(double)

    if single_length > 0 and double_length > 0:
        print(single_length // 2 + double_length)

    elif single_length > 0 and double_length == 0:
        print(single_length // 2)

    elif single_length == 0 and double_length > 0:
        print(double_length)
