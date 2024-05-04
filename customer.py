import csv

def display_customer():
    print('     Customer Section')
    print("➕Press 1 to add customer")
    print("➕Press 2 to search customer")
    print("➕Press 3 to delete customer")
    print("➕Press 4 to update customer")
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
        case default:
            print("Wrong Options")
            display_customer()
            
def add_customer():
    with open('D://VS Coding//Python/Day29//customer.csv','r') as writeFile:
        columns = ['id','name','DOB','city','phone_number']

def search_customer():
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        # columns = ['id','name','DOB','city','phone_number']
        csv_reader = csv.DictReader(readFile)  
        for i in csv_reader:
            print(i)
def delete_customer():
    pass

def update_customer():
    pass

