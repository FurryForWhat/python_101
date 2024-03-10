def calculation(a :int, b :int):
    global_list = []
    another_list = []
    for i in range(a):
        a = []
        for j in range(b):
            # another_list.append(i * j)
            global_list.append(i * j)
        a.append(global_list)
    print(a)

if __name__ == '__main__':
    try:
     while True:
        a = int(input(":"))
        b= int(input(':'))
        calculation(a,b)
    except KeyboardInterrupt :
       print('Program Exit')


