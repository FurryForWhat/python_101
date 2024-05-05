import csv

def id_generator():
    with open('D://VS Coding//Python/Day29//customer.csv','r') as readFile:
        csv_reader = csv.DictReader(readFile)
        index = 1
        for i in csv_reader:
            if index == int(i['id']):
                index += 1
    return index

def OTP():
    pass

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