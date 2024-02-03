Numbers=(1,2,3,4,5,6,7,8,9)
even=0
odd = 0
my_array= list(Numbers)

for index in range(len(my_array)):
    if my_array[index] % 2 == 0:
        even += 1
    else :
        odd += 1

print('Total :', even + odd)
print('Totel even Number : ',even)
print('Totel odd Number : ',odd)
#prime number