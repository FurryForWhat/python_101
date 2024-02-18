# a = 1000
# b = a / 0
# print(b)


try:
    x = 10
    print(x)
    a = 1000/ 12
except ZeroDivisionError:
    print("You just add O after division")
except NameError:
    print("You just add name without delcaration")
except :
    print("You just got some error")