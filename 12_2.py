print("This is login form")
login_email = str(input("Enter your email:"))
login_pass = str(input("Enter your password:"))

file_user = open("D:\\VS Coding\\Python\\Day12\\user_info.txt",'r')

for i in file_user:
    user_id,user_name,user_email,user_pass = i.split()
    # print(user_id)
    # print(user_name)
    # print(user_email)
    # print(user_pass)
    
    if login_email == user_email and login_pass == user_pass:
        print('Welcome back Mr.{}'.format(user_name))  