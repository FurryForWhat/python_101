import display

owner = ['Andrew','1234567']

def login():    
    user_flag = True
    while user_flag :
        user_name = input("Username :")
        user_password = input("Password :")
        if user_name != owner[0]:
            print('❌Wrong Username')
        elif user_password != owner[1]:
            print('❌ Wrong Password')
        else:
            user_flag = False
            print('Login Success')
            display.display()
            
            
