def firstFun():
    a = 15
    my_list =[]
    for i in range(1,a+1):
        my_list.append(i)

    my_list = map(str,my_list)
    print(','.join(my_list))

# def secondFun(a):
#     my_list =[]
#     if a == 1:
#         return 1
#     else:
#         result = secondFun(a-1)
#         print(result)

def outFunction(num):
   if num == 1:
       return 1
   else:
       print(outFunction(num-1))
        


outFunction(15)