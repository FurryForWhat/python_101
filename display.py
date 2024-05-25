import sys
import customer
import tools

def display():
    flag = True
    while flag:
        print('*'*115)
        tools.print_in_middle('Display Section⭕')
        print('Press 1 to Customer Section')
        print('Press 2 to Medicine Section')
        print('Press 3 to Exit')
        user_input = int(input('➡️  '))
        match user_input:
            case 1:
                customer.display_customer()
            case 2:
                pass
            case 3:
                print('Program exit.')
                sys.exit()
            case default:
                print('❌ Wrong Options')
                display()
                
display()