email = input("Enter ur gmail:") #ncc@gmail.com
name = input("Enter name:")
password= input("Enter password:")
re_pass= input("Retype password:")

if( re_pass == password):
     print("Your password is correct")
     print("Ur email :"+email+" your name:" + name+" and password:"+password)
     
else:
    print("wrong matching")