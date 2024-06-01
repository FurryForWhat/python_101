import csv
import tools
import os

def display_customer():
    tools.print_in_middle('Customer Section')
    tools.print_with_borders("➕Press 1 to add customer")
    tools.print_with_borders("➕Press 2 to search customer")
    tools.print_with_borders("➕Press 3 to delete customer")
    tools.print_with_borders("➕Press 4 to update customer")
    tools.print_with_borders("➕Press 5 to exit")
    try:
        user_choice = int(input("➡️  "))
    except ValueError as e:
        print('Invalid Input , Use only number.')
        display_customer()
    match user_choice:
        case 1:
            add_customer()
        case 2:     
            search_customer()
        case 3:
            delete_customer()
        case 4:
            update_customer()
        case 5:
            return
        case default:
            print("Wrong Options")
            display_customer()
            
def add_customer():
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        
        csv_reader = csv.DictReader(readFile)
        cu_name = input('Enter customer name->')
        
        dob_flag = False
        while dob_flag == False:
            cu_dob = input('Enter customer Date of Birth (eg. \"12-Feb-1988\")->')
            dob_flag = tools.dob_valid(cu_dob)
            if dob_flag:
                cu_city= input('Enter City->')
                phone_flag = False
                
                while phone_flag == False:
                    cu_ph = input('Enter Phone number->')
                    phone_flag = tools.ph_valid(cu_ph)
                    if phone_flag:
                        for i in csv_reader:
                            if cu_name == i['name'] and cu_dob == i['DOB']:
                                print('❌User already exists')
                                display_customer()

                        with open('D://VS Coding//Python/Day29//customer.csv','a',newline='') as writeFile:  
                                    columns = ['id','name','DOB','city','phone_number']
                                    csv_writer = csv.DictWriter(writeFile,fieldnames=columns)
                                    cu_id = tools.id_generator()
                                    csv_writer.writerow({'id':cu_id,'name':cu_name,'DOB':cu_dob,'city':cu_city,'phone_number':cu_ph})
                                    print('Customer added successfully!!!')       
                        display_customer()
            else:
                print('Invalid format , try again!!!!')

def search_customer():
    user_name = input("Enter username to search->")
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        csv_reader = csv.DictReader(readFile)
        flag = True
        for i in csv_reader:
            if i['name'] == user_name:
                flag = False
                print('User found📛')
                print('➡️',i)
                display_customer()
        if flag == True:
            print('❌ User not found!!!')
            search_customer()

def delete_customer():
    user_name = input("Enter username to search->")
    flag = True
    user_change = True
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        with open('D://VS Coding//Python/Day29//temp.csv','w+',newline='') as tempFile:
            read_csv = csv.DictReader(readFile)
            columns = ['id','name','DOB','city','phone_number']
            write_csv = csv.DictWriter(tempFile,fieldnames=columns)
            write_csv.writeheader()
            for i in read_csv:
                if i['name'] == user_name:

                    print('User name',i['name'],'found!!!!')
                    print('Are you sure to delete user:',i['name'],'?')
                    user_deleter = str(input('Y/N➡️  '))
                    v_2 = user_deleter.lower()
                    
                    if v_2 == 'y' or v_2 == 'yes':
                        flag = False
                        print('User deleted successfully')
                    elif v_2 == 'n' or v_2 == 'no':
                        write_csv.writerow(i) 
                        user_change = False
                        
                else:
                    write_csv.writerow(i)

    if flag == True and user_change == True:
        print('❌ User not found!!!')
        display_customer()
    elif flag == True and user_change == False:
        print('No data was changed')
        os.remove('D://VS Coding//Python/Day29//customer.csv')
        os.rename('D://VS Coding//Python/Day29//temp.csv','D://VS Coding//Python/Day29//customer.csv')
        display_customer()
    else:
        os.remove('D://VS Coding//Python/Day29//customer.csv')
        os.rename('D://VS Coding//Python/Day29//temp.csv','D://VS Coding//Python/Day29//customer.csv')
        display_customer()
        

def update_customer():
    user_name = input("Enter username👤 ->")
    flag = True
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        with open('D://VS Coding//Python/Day29//temp.csv','w+',newline='') as tempFile:
            columns = ['id','name','DOB','city','phone_number']
            write_csv = csv.DictWriter(tempFile,fieldnames=columns)
            write_csv.writeheader()
            read_csv = csv.DictReader(readFile)
            for user in read_csv:
                if user_name == user['name']:
                    flag = False
                    rand_otp = tools.OTP()
                    print(f'user :{user['name']} found🔔')
                    print('What u want to update?')
                    print('Press 1 to update name💩')
                    print('Press 2 to update birthday🎂(eg. \"12-Feb-1988\")')
                    print('Press 3 to update city🏙️')
                    print('Press 4 to update phone🤙🏻')
                    u_input = int(input('➡️  '))
                    if u_input == 1:
                        new_name = input('new name: ')
                        print(rand_otp)
                        otp = input('Enter OTP: ')
                        if otp == rand_otp:
                            user['name'] = new_name
                    elif u_input == 2:
                        new_name = input('new birthday: ')
                        print(rand_otp)
                        otp = input('Enter OTP: ')
                        if otp == rand_otp:
                            user['DOB'] = new_name
                    elif u_input == 3:
                        new_name = input('new city: ')
                        print(rand_otp)
                        otp = input('Enter OTP: ')
                        if otp == rand_otp:
                            user['city'] = new_name
                    elif u_input == 4:
                        new_name = input('new phone number: ')
                        print(rand_otp)
                        otp = input('Enter OTP: ')
                        if otp == rand_otp:
                            tools.ph_valid(new_name)
                            user['phone_number'] = new_name
                    else:
                        print('Invalid Input , Try again❌')
                        update_customer()
                write_csv.writerow(user)                
    if flag == True:
        print('User not found❌❌❌')
    else:
        os.remove('D://VS Coding//Python/Day29//customer.csv')
        os.rename('D://VS Coding//Python/Day29//temp.csv','D://VS Coding//Python/Day29//customer.csv')
        print('User data updated successfully✅✅✅')
        display_customer()

    
display_customer()