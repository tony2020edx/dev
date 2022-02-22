

def satisfying_condition(x):

    if x.count('a') >  x.count('b') and x.count('a') > x.count('c'):
        return True
    else:
        return False

def gen_substring(text,n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if satisfying_condition(text[i:j]) == True:
                count = len(text[i:j])
                break
    return count


t = int(input())

for i in range(t):
    n = int(input()) + 1
    text = input()
    print(gen_substring(text,n))













