my_data = {}

def loading_file():
    try:
        file_one = open('D:\\VS Coding\\Python\\Day13\\Day13.txt','r') #write mode append

        my_data = {}
        
    except FileNotFoundError as error:
        print('No file found',error)

loading_file()