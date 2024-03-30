import string
import calendar

def Finding(user_data : str):
    vowelCount = 0
    consonantCount = 0
    mydata = 'aeiouAEIOU'
    mydata2 = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'
    for i in user_data:
        for j in range(0,len(mydata)):
            if i == mydata[j]:
                vowelCount += 1
        for z in range(0,len(mydata2)):
            if i == mydata2[z]:
                consonantCount += 1

    print('Total length is',len(user_data))
    print('vowels',vowelCount)
    print('consonant', consonantCount)

def find_date(year,month,day):
    a = calendar.weekday(year,month,day)
    print(calendar.day_name[a].upper())
    
    
find_date(2024,3,22)

# Finding('In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted')
          