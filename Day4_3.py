x, y=input("Enter two values: ").split()

# x = int(x)
# y = int(y)

if x > y :
    print("{} is greater than {}".format(x, y))
elif x < y:
    print("{} is less than {}".format(x, y))
elif x == y:
    print("{} is equal to {}".format(x,y))
else :
    print("Something Wrong")

