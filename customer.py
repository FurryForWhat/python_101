import csv
import tools
import display

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
            display.display()
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
    pass

def update_customer():
    pass

add_customer()