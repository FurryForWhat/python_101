import string

def Finding(user_data : str):
    vowelCount = 0
    consonantCount = 0
    mydata = 'aeiouAEIOU'
    for i in range(len(mydata)+1):
        for j in range(i,len(user_data)+1):
            if user_data[j] == mydata[i]:
                vowelCount += 1
            else:
                consonantCount += 1

    print('vowels',vowelCount)
    print('consonant', consonantCount)
                


def fibon(number: int):
    a,b = 0,1
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number < 0:
        return 'can\'t include negative number'
    else:
        add_list = []
        for i in range(2,number +2):
             c = a + b
             a, b = b, c
             add_list.append(c)
        return add_list

Finding('Telephone')

