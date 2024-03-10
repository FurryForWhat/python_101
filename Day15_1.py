def doubleValue(number : str) -> dict :  #number = '5'
    number = int(number)  # number = 5
    my_dict = {}
    for i in range(1,number+1):  # 1 -5 ,1 2 3 4 5
        key = i
        value = i * i
        my_dict.update({key:value})
    return my_dict

def acceptOneVariable(data_one):
    a = data_one
    b = str(data_one)
    return a,b

if __name__ == '__main__':
    first, seconde = acceptOneVariable(1)    
    print(first)
    print(seconde)
