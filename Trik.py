
position = '1'

route = input()

for ch in route:
    if ch == 'A':
        if position == '1':
            position = '2'
        elif position == '2':
            position = '1'
    elif ch == 'B':
        if position == '2':
            position = '3'
        elif position == '3':
            position = '2'

    elif ch == 'C':
        if position == '1':
            position = '3'
        elif position == '3':
            position = '1'

print(position)
