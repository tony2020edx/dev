import itertools

res = []

for i in range(0, 10):

    k = list(itertools.product(['a', 'b', 'c'], repeat=i))

    for j in k:
        if len(j) >= 2 and j.count('a') > j.count('b') and j.count('a') > j.count('c'):
            if j not in res:
                res.append(''.join(j))

new_res = []

for j in res:
    if j.count('a') == 3 and j.count('bb') == 1 and j.count('cc') == 1 and j[0] == 'a' and j[-1] == 'a':
        new_res.append(j)
    if j.count('a') == 2 and j.count('b') == 1 and j.count('c') == 1 and j[0] == 'a' and j[-1] == 'a':
        new_res.append(j)
    if j.count('a') == 2 and j.count('b') == 0 and j.count('c') == 0 and j[0] == 'a' and j[-1] == 'a':
        new_res.append(j)
    if j.count('a') == 2 and j.count('b') == 1 and j.count('c') == 0 and j[0] == 'a' and j[-1] == 'a':
        new_res.append(j)
    if j.count('a') == 2 and j.count('b') == 0 and j.count('c') == 1 and j[0] == 'a' and j[-1] == 'a':
        new_res.append(j)



print(len(new_res))
print(new_res)

new_new_res = ['aa']

for i in new_res:
    if i.count('aa') == 0:
        new_new_res.append(i)
print(new_new_res)
print(len(new_new_res))












