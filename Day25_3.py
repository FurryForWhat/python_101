#Closure

def power(pow:int):
    
    def number(num:int):
        return num ** pow
    return number


power_2_of= power(2)
power_of_3 = power(3)


print(power_of_3(33))




