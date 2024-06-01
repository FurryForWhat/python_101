import sys
import customer
import tools
import medicine
def display():
    flag = True
    while flag:
        tools.print_in_middle('Display Section⭕')
        tools.print_with_borders('Press 1 to Customer Section')
        tools.print_with_borders('Press 2 to Medicine Section')
        tools.print_with_borders('Press 3 to Exit')
        user_input = int(input('➡️  '))
        match user_input:
            case 1:
                customer.display_customer()
            case 2:
                medicine.display_medicine()
            case 3:
                print('Program exit.')
                sys.exit()
            case default:
                print('❌ Wrong Options')
                display()
