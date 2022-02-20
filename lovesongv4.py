



alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

n, q = map(int, input().split())

s = input()

for i in range(q):

    l, r = map(int, input().split())

    sub_segment = s[l - 1:r]  # generate sub sequence

    result = 0

    set_sub_segment = list(dict.fromkeys(sub_segment ))

    for j in set_sub_segment:
        count = sub_segment.count(j)
        data = alphabets.index(j) + 1
        data = count * data
        result += data

    print(result)