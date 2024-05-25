import csv
import tools
import os

def display_customer():
    print('     Customer Section')
    print("➕Press 1 to add customer")
    print("➕Press 2 to search customer")
    print("➕Press 3 to delete customer")
    print("➕Press 4 to update customer")
    print("➕Press 5 to exit")
    user_choice = int(input("➡️  "))
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
        cu_dob = input('Enter customer Date of Birth->')
        cu_city= input('Enter City->')
        
        flag = False
        
        while flag == False:
            cu_ph = input('Enter Phone number->')
            flag = tools.ph_valid(cu_ph)
            if flag:
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

def search_customer():
    user_name = input("Enter username to search->")
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        csv_reader = csv.DictReader(readFile)
        flag = True
        for i in csv_reader:
            if i['name'] == user_name:
                flag = False
                print('➡️',i)
                display_customer()
        if flag == True:
            print('❌ User not found!!!')
            display_customer()

def delete_customer():
    user_name = input("Enter username to search->")
    flag = True
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
                    user_deleter = input('Y/N➡️  ')
                    if user_deleter == 'Y':
                        flag = False
                        print('User deleted successfully')
                    elif user_deleter == 'N':
                        write_csv.writerow(i) 
                else:
                    write_csv.writerow(i)

    if flag == True:
        print('❌ User not found!!!')
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
                    print('Press 2 to update birthday🎂')
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
        
