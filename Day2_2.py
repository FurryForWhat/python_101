
print("Hello I'm website!!!")
print('Enter your name.')
user_name = input('Name: ')

print("Entr your gmail.")
user_gmail = input('Gmail:')

print ("Enter password")
user_pass = input ('Pass:')

print("Enter phone number")
user_phNum = int(input("phNum: ")) #type casting

print(" Your name is {} ".format(user_name) ,"your gmail is {}".format(user_gmail) ," and password is {}. Phone number is {}".format(user_pass,user_phNum))  #placeholder , curly brace
print ( "Your name is {2} , your gmail is {3} and your password is {1}. Phone number is {0}".format (user_phNum, user_pass, user_name,user_gmail))

