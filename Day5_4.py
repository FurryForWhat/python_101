a,b,c,d,e=input("enter values :").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e= int(e)
my_list = [a,b,c,d,e]

i = 0
U_10 = 0
A_10 = 0
length = len(my_list)

while  length != 0:
    if my_list[i] <= 10:
        U_10 +=1
    elif my_list[i] > 10:
        A_10 +=1
    i += 1    
    length -= 1
        
print("Under 10 is :",U_10)
print("Above 10 is :",A_10)