n, q = map(int, input().split())

def change(text, position, ch):
    text = text.replace(text[position-1], ch,1)
    return text

ui = input()

for z in range(q):

    pos , ch = map(str, input().split())

    pos= int(pos)

    text = change(ui, pos, ch)

    count = text.count('abc')
    print(count)









