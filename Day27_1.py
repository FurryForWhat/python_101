def person(name: str):
    def weight(my_weig):
        print(my_weig,"Kg")
        
    # def height(my_heig):
    #     print(my_heig)
    return weight 

John = person("John")
John_weight = John(50)
John_weight