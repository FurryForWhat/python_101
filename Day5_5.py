email = 'ncc@gmail.com'
password = 'NationalCyberCity'

u_email = input('email:->')
u_pass = ''

while u_pass != password:
    u_pass = input('pass:->')
    if u_pass != password:
        print("Wrong pass, try again!")

print('Log in Success')