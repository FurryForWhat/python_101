import customer

def display():
    print('Press 1 to Customer Section')
    print('Press 2 to Medicine Section')
    user_input = int(input('➡️  '))
    match user_input:
        case 1:
            customer.display_customer()
        case 2:
            pass
        case default:
            print('❌ Wrong Options')
            display()

