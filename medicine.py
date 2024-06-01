import tools


def display_medicine():
    tools.print_in_middle("Medicine Section")
    print("➕Press 1 to add medicine")
    print("➕Press 2 to search medicine")
    print("➕Press 3 to delete medicine")
    print("➕Press 4 to update medicine")
    print("➕Press 5 to purchase medic list")
    print("➕Press 6 to main menu")
    user_input = int(input("Enter Here ➡️ "))
    if user_input == 1:
        add_medicine()
    elif user_input == 2:
        search_medicine()
    elif user_input == 3:
        delete_medicine()
    elif user_input == 4:
        update_medicine()
    elif user_input == 5:
        to_purchase()
    elif user_input == 6:
        return
    else:
        print('Invalid Options, Try again❌❌❌')
        display_medicine()

def add_medicine():
    tools.print_in_middle("Please register Medical Product💊")
    medic_name = input('Add Name📛:')
    medic_id= input('Add ID🆔:')
    sale= input('Add Sale📈:')
    quantity= input('Add Quantity➕:')
    company= input('Add company🫂:')
    director= input('Add Sale Director🙎🏻‍♂️:')
    status= input('Add Status📑:')
    remark= input('Add Note🔖:')
    data_format = ['medic name','medic ID','sale','quantity','company name','sale_director','status','note']
    log= [medic_name,medic_id,sale,quantity,company,director,status,remark]
    tools.mongo_format(data_format,log)
    display_medicine()
    
def search_medicine():
    client,database,collection  = tools.mongo_connect()
    # print(client.list_collection_names())

    flag = True
    while flag:
        s_medic = input('Enter Medical Product Name💊 :')
        s_id = input('Enter Medical ID: ')
        for i in collection.find({},{"_id":0,"medic name":1,"medic ID":1}):
            if s_medic == i['medic name'] and s_id == i['medic ID']:
                flag = False
                tools.print_with_borders('Medical Product Found✅✅')
        if flag:
            tools.print_with_borders('No Product Found ❌❌')
            ans = input('Do you want to exit? Y/N:')
            if ans == 'Y':
                flag = False

def delete_medicine():
    client,database,collection  = tools.mongo_connect()
    flag = True
    while flag:
        s_medic = input('Enter Medical Product ID :')
        for i in collection.find({},{"medic ID":1}):
            if s_medic == i["medic ID"]:
                flag = False
                ans= input('Product Found! Do u want to delete it? Y/N:')
                if ans == 'Y':
                    query = {"medic ID": s_medic}
                    collection.delete_one(query)
                    print('Deleted✅✅✅')
                    
def update_medicine():
    client,database,collection  = tools.mongo_connect()
    flag = True
    while flag:
        s_medic = input('Enter Medical Product ID :')
        for i in collection.find({},{"medic name":1,"medic ID":1,"sale":1,"quantity":1,
                                     "sale_director":1,"company name":1,"status":1,"note":1}):
            if s_medic == i["medic name"]:
                flag = False
                print("Press 0 to update Note: ")
                print("Press 1 to update medical name: ")
                print("Press 2 to update medical ID: ")
                print("Press 3 to update medical sale: ")
                print("Press 4 to update medical quantity: ")
                print("Press 5 to update medical company name: ")
                print("Press 6 to update medical sale director: ")
                
                u_in = 10
                while u_in > 8:
                    u_in = int(input("Enter Here➡️ :"))
                    if u_in == 1:
                        print('updated')
                    elif u_in == 2:
                        print('updated')
                    elif u_in ==3:
                        print('updated')
                    elif u_in == 4:
                        print('updated')
                    elif u_in == 5:
                        print('updated')
                        user_company = input("Please fill new company name: ")
                        pre_data = i["company name"]
                        checker = {"company name":pre_data}
                        newvalue = { "$set": { "company name": user_company } }
                        collection.update_one(checker,newvalue)
                        
                    elif u_in == 6:
                        print('updated')
                    elif u_in == 0:
                        print('updated')
                    else:
                        print("Invalid Input Try again!!!")
        

                    

def to_purchase():
    pass
