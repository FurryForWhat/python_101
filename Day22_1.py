def Factorial(num): #5 4 3 2 1
    if num == 1:
        return 1
    else:
        return num + Factorial(num-1)

def numberFun(start,end):
    if start > end:
        return 1
    elif start == end:
        print(start)
    else:
        print(start,end=',')
        numberFun(start+1,end)
    
def loopFun(num):
    if num == 1:
        return 1
    else:
        numberFun(1,num)

# def fibonacci():

def addList(my_list : list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + addList(my_list[1:])

# print(addList([1,2,8,12,21]))

#def power(num,pow),