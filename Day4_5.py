x = int(input("Enter number:"))

key = int(input("Press 1 to add 10\nPress 2 to add 5\n->"))
#match case
match key:
    case 1:
        x += 10
        print("Result is->",x)
    
    case 2:
        x += 5
        print ("Result is->",x)
    case default:
        print("Invalid number")