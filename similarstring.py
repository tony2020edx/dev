
def generate_sub(s,length):
    for i in range(len(s) - length + 1):
        yield s[i:i+length]




p = list(generate_sub("1110000",4))
print(p)

res = []

for i in range(len(p)):

    res.append(p[i][i])

print(res)







