import csv
from random import randint
import pymongo


def id_generator():
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        csv_reader = csv.DictReader(readFile)
        index = 1
        for i in csv_reader:
            if index == int(i['id']):
                index += 1
    return index

def OTP():
    rand_number = randint(100000,999999)
    return str(rand_number)

def dob_valid(user_dob:str):
    Day,Month,Year = user_dob.split('-')
    calendar_flag = calendar_format(Day,Month,Year)
    if calendar_flag :
        return True
    else:
        return False
    
def ph_valid(user_phone):
    if len(user_phone) == 11 and int(user_phone[0]) == 0 and int(user_phone[1]) == 9:
        if int(user_phone[2]) == 7:
            print('Atom phone number')
        elif int(user_phone[2]) == 2:
            print('MPT phone number')
        elif int(user_phone[2]) == 9:
            print('Ooredoo phone number')
        return True
    else:
        print('Invalid Phone Number')
        return False

def print_in_middle(text): #Display Section_    *                  hi                *
    max = 100
    left_padding = (max - len(text) - 4) // 2   
    right_padding = left_padding
    print(f"{'*'*max}")
    print(f'| {' '*left_padding}{text}{' '*right_padding} |')
    
def print_with_borders(text):
    max = 100
    right_padding = max - (len(text) + 3)
    print(f'| {text}{' '*right_padding}|')
    
def mongo_format(format,data): #id,medic_name,medic_id,sale,quantity,company,sale_director,status,remark  // user_data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database = myclient['Inventory']
    collection = database['medical_list']
    
    data_log = {}
    
    for i in range(len(format)):
        data_log.update({format[i]:data[i]})
        
    collection.insert_one(data_log)
    print('Data all added successfully✅✅✅')
    
def mongo_connect():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client['Inventory']
    collection = database['medical_list']
    return client,database,collection

def calendar_format (in_day,in_month,in_year):
    in_year = int(in_year)
    # in_month = int(in_month)
    in_day = int(in_day)
    leap_year = False
    month_flag = False
    if in_year % 4 == 0:
        leap_year = True
    cal_dic = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,
               'Sep':30,'Oct':31,'Nov':30,'Dec':31}
    
    if leap_year:
        for i,j in cal_dic.items():
            if i == 'Feb':
                j = 29
            cal_dic.update({i:j})
    
    for i,j in cal_dic.items():
        if in_month == i:
            month_flag = True
            if 1<= in_day <=j :
                return True
            else:
                print('Invalid Day')
                return False
    
    if month_flag == False:
        print('Invalid Month')
        return False        

