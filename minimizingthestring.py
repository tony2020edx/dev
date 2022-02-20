n=int(input())
text =input()

for i in range(n-1):
    if text[i]>text[i+1]:
        print(text[0:i]+text[i+1:n]) #list slicing logic
        exit()
print(text[0:n-1])