def rev(a: list):
    b = []
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    b = map(str,b)
    # print(tuple(b))
    return ('\n'.join(b))


if __name__ == '__main__':
    print(rev([1,2,4,3,5,7,10,12]))
    # print(1,2,3,sep = '!')