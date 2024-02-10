def restruant(item):
    e_count = 0
    for i in item:
        if i == 'e':
            e_count += 1
        else:
            pass
    return e_count

x = restruant('Fried Rice')
print(x)
