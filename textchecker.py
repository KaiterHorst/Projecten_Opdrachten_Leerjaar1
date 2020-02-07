a = input('geef een string:')
b = input('geef nog een string:')

c = 0
while a[c] == b[c]:
    c += 1

print('Het eerste verschil zit op index', c)