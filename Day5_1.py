x = int(input('1: breakfast \n 2: not breakfast'))
if x == 1:
    print("Done breakfast")
    y = int(input('1: for Shower\n2: for uniform'))
    if y == 1:
        print("Start wearing uniform")
        z = int(input ('1:for email checking\n 2:go to work'))
        if z==1:
            print("Checking email and go to work")
        else :
            print("Go to Work")
    else:
        print("Go to Work")

else:
    print("Doesn't breakfast")
    print("Go to Work")