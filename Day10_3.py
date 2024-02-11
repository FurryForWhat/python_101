import math
import random
a = int(input('Enter minimum value->')) # 10
b = int(input('Enter maximum value->')) # 1
flag = True
if a >= b:
    print('Wrong Format!')
    exit(0)
else:
    x = random.randint(a,b)
    
    while flag:
        numOne= int(input('Gussing number->'))
        if x == numOne:
         print('Right Answer!!')
         flag = False
        elif numOne > x:
         print('Guessing number is greater than.')
        else:
         print('Guessing number is less than.')
