def fun_1(firstdata : str) -> int:  # "12, 11 , 15"
    a, b , c = firstdata.split(',')
    a = int(a) # 12
    b= int(b)  #11
    c = int(c) # 15
    
    if a > b:
        if a > c:
            return a
        else:
            return c
    else: 
       if b > c:
           return b
       else :
           return c
       
def list_1(data: list):
    a = len(data)
    while a > 2:
        print(data.pop(2))
        a -= 1
        
        
if __name__ == '__main__':
    # list_1([1,2,3,6,7,43,2])
    
   a =  input(':').split(' ')
   list_1(a)