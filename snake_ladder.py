import random



snake ={18:3,36:5,54:7,93:73,95:55,97:37,99:2}
ladder = {4:24,6:46,8:68,9:92,23:98,45:96}

def rolldice():
    return random.randint(1,6)

def move_player(position):
    dice=rolldice()
    position += dice

    if position >100:
        position -=dice
        return position
    
    if position in ladder:
        print(f"you got ladder position is {ladder[position]}")
        position = ladder[position]
    elif position in snake:
        print(f"you got snake position is {ladder[position]}")
        position=ladder[position]
    return position


def play_game():
    print("start game.......")

    a,b = 0,0

    while True:
        input("\n player 1,press enter to roll the dice.....")
        a=move_player(a)
        print(f"player 1 is {a}")

        if a == 100:
            print("\n player i wins")
            break

        input("\nplayer 2,press enter to roll the dice....")
        b=move_player(b)
        print(f"plyer 2 now in {b}")

        if b == 100:
            print("\nplayer 2 is win")
            break

play_game()