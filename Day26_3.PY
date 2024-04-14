def play_game(player):
    coins = 10
    
    def shooting():
        nonlocal coins
        coins -= 1
        if coins == 0:
            print(f'{player} have left {coins} coins, Fill more')
        elif coins <2 :
            print(f"{player} can play anymore, {coins} coin")
            exit(0)
        else:
            print(f'{player} have left {coins} coins')
    return shooting

Kyaw_Kyaw = play_game("Kyaw Kyaw")
Kyaw_Swar = play_game("Kyaw Swar")
Ni_Ni = play_game("Ni Ni")


Kyaw_Kyaw()
Ni_Ni()
Kyaw_Swar()
