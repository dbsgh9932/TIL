for x in range(4):
    for y in range(5):
        print('*',end='')
    print()

for x in range(5):
    for y in range(5):
        if y<=x:
            print('*',end='')
    print()

for x in range(5):
    for y in range(5):
        if y>=x:
            print('*',end='')
    print()

