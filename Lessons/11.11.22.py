import random


 # создать колоду
# перемещать колоду 
# тянуть карты из колоды 
# складывать очки с вытянутой картой 
# если игрок набрал больше 21 он проиграл 
# если равно 21 он выиграл 
# если меньше 21 он может решить брать карту или нет 
#
def draw_a_card():
    if deck:
        card = deck.pop(-1)
    else:
        print("колода пуста")
    card = None
    return card
def update_score(score):
    current_score = player_score + score 
    print(f"у вас {current_score} очков")
    return current_score 
def decision():
    While True: 
        des = input('брать карту? y/n')
        if des == 'y':
            return True
        elif des == 'n':
            return False
        else: 
            print("вы ввели недопустимую команду!")
            continue 





deck = [2,3,4,5,6,7,8,9,10,11]*4
random.shuffle(deck)
# print(deck)
# print(deck[-1]) 
b_continue = True
while b_continue:
    card = draw_a_card()
    if card != None:
        print(card)
        player_score = update_score(card)
    else:
        break


 