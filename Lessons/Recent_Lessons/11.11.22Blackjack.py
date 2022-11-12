import random
# Создать колоду
# Перемешать колоду
# Тянуть карты из колоды
# Складывать очки с вытянутой картой
# Если игрок набрал больше 21 он проиграл
# Если ровно 21 он выиграл
# Если меньше 21, он может решить, брать карту или не брать
# 
def draw_a_card():
    if deck:                    #if len(deck)!= 0
        card = deck.pop(-1)
    else:
        print('Колода пуста')
        card = None
    return card

def update_score(score):
    current_score = player_score + score
    print(f'У вас {current_score} очков')
    return  current_score

def decision():
    while True:
        des = input('Брать карту? y/n')
        if des == "y":
            return True
        elif des == "n":
            return False
        else:
            print("Вы ввели недопустимую команду! ") 
            continue       

def b_win(score):
    if score ==  21:
        print('Вы победили!')
        return True
    elif score > 21:
        print('Вы проиграли!')
        return False
    elif score < 21:
        return None        


deck = [2,3,4,6,7,8,9,10,11]*4
random.shuffle(deck)



b_continue = True
player_score = 0
while b_continue:
    
    card = draw_a_card()

    if card != None:
        print(card)
        player_score = update_score(card)
        win = b_win(player_score)
        if win == None:
            pass
        elif win == False:
            break
        elif win == True:
            break
    else:
        break
    b_continue = decision()

print('Игра окончена')    