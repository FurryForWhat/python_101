import math
import random
a = int(input('Enter minimum value->')) # 10
b = int(input('Enter maximum value->')) # 1

if a >= b:
    print('Wrong Format!')
    exit(0)
else:
    x = random.randint(a,b)
    chances = round(math.log(b -a +1,2))
    spend_chances = 1
    while spend_chances <= chances :
        spend_chances += 1
        numOne= int(input('Gussing number->'))
        if x == numOne:
         print('Right Answer!!')
         exit(1)
        elif numOne > x:
         print('Guessing number is greater than.')
        else:
         print('Guessing number is less than.')
    #code