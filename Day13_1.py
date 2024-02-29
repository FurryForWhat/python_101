my_data = {}
with  open('D:\\VS Coding\\Python\\Day13\\Day13.txt','r') as file_one:
    data = file_one.readlines()
    for i in data:
        myData = i.split(' ')
        data_format = {len(my_data)+1:{'id':myData[0],'name':myData[1],'email':myData[2],'pass':myData[3]}}
        my_data.update(data_format)
        
print(my_data)
