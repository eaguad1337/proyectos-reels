items = ['a', 'c', 'd']

for item in items:
    if item == 'b':
        items.remove(item)
    else:
        print(item)
