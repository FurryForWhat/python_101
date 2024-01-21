x = int(input("Enter Age:"))
y = int(input("Press 1 License On\nPress 0 License OFF:"))

if( x > 18 and y == 1):
    print("You can drive anywhere!")
elif ( x < 18 and y == 1):
    print("You can drive local area!")
elif ( x > 18 and y == 0):
    print("You can drive but u would arrest!")
elif( x < 18 and y== 0):
    print("Don't touch the bike")
else:
    print("invalid option!")

