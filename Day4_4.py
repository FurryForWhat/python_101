print("Mini-calculator")
x = int(input("Enter first number:"))
y= int(input("Enter Second number:"))

z = int(input('Press 1 to Sum\nPress 2 to Subtract\nPress 3 to Multiple\nPress4 to Division\nPress 5 to Modulus\n->'))
#if elif else
if z == 1:
    result = x + y
    print("Result is: ",result)
elif z == 2:
    result = x - y
    print("Result is: ", result)

elif z== 3:
    result = x * y
    print("Result is :",result)    
elif z== 4:
    result = x / y
    print("Result is :",result)    
elif z== 5:
    result = x % y
    print("Result is :",result)    
else:
    print("Invalid option!")
