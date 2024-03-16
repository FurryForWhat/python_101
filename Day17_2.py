def pass_valid(a :str ):
    s_letter = 0
    c_letter = 0
    n_letter = 0
    special = 0
    if 6 <= len(a) <= 16: # len(a) = 6
        for i in range(len(a)):
            if 97 <= ord(a[i]) <= 122:
                s_letter += 1
            elif 65 <= ord(a[i]) <= 90:
                c_letter += 1
            elif 48 <= ord(a[i]) <= 57:
                n_letter += 1
            elif a[i] == '$' or a[i] == '#' or a[i] == '@':
                special += 1
            else:
                return 'Invalid character contain'
        if s_letter != 0 and c_letter != 0 and n_letter != 0 and special != 0:
            return 'Valid Password'
        else:
            return 'Invalid Password'
    else:
       return 'Password should be minimum length of 6 and maximum legth of 16'  

if __name__ == '__main__':
    while True:
        a = input('>')
        print(pass_valid(a))  # 'Hi123@'