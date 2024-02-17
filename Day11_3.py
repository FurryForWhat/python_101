
def flightTicket(amount: int):
    print('Ticket Section!!')
    ticket_select = input('Press 1 to Myanamr to LA\nPress2 to Myanmar tor Singapore\nPress 3 to Singapore to Myanmar\nPress 4 to LA to Myanmar\n->')
    ticket_select = int(ticket_select)
    if ticket_select == 1:
        y_n= input('The price is $500\nBuy?(Yes or No)')
        if y_n == 'Yes' or y_n == 'yes':
            if amount>= 500:
                amount -= 500
                return 'Ticket 1', amount
            else:
                return 'You can\'t buy',amount
        else:
            flightTicket()
    elif ticket_select == 2:
        pass
    elif ticket_select == 3:
        pass
    elif ticket_select == 4:
        pass
    else:
        print('Invalid Option')
        flightTicket() #recursive function
        
def hotelBooking(amount: int):
    hotel_choice = input('Press 1 for Hotel A\nPress2 for Hotel B\nPress 3 for Hotel C\n->')
    match int(hotel_choice):
        case 1:
            print("Welcome to Hotel A")
            #Single, Double, Family (High Grade) Swimming pool, gym, golf, asian/europe resturant, luxury item , ferry service?
        case 2:
            print('Welcome to Hotel B')
            #Single, Double, Family(middle Grade) gym, resturant,ferry service?
        case 3:
            print('Welcome to Hotel C')
            #Single, Double, Family  (Low Grade) !nothing 
        case default:
            print('Invalid Option')
            hotelBooking()
def ferry():
    pass


if __name__ == "__main__":
    print('Welcome to Our Service!\n How Can I help u!')
    
    user_input = input("Press 1 for flight ticket\nPress 2 for Hotel Booking\nPress 3 for Ferry\nPress 4 for Exit\n->")
    money = 1000
    file_one= open('D:\\VS Coding\Python\\Day11\\file.txt', 'a')
    match int(user_input):
        case 1:
            x,y = flightTicket(money)
            print("Your items: {} {}".format(x,y))
            file_one.write("Ticket: "+x+" Cash-Back: "+str(y)+'\n')
        case 2:
           x,y= hotelBooking(money)
           print("Your items: {} {}".format(x,y))
        case 3:
            ferry(money)
            
        case 4:
            exit(0)
        case default:
            print('Invalid Option!!!')
    file_one.close()
