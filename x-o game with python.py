import sys
import time

# simple x-o game with python created from Asem Abdallah
# this is a simple game by beginner

""" X-O Game file 
this is file is created by Asem Abdallah"""



# Function for check the winner
def check_winner():

    if list1[0] == list1[1] == list1[2]:
        print(f"player {list1[0]} is win")
        close_and_sleep()

    elif list1[3] == list1[4] == list1[5]:
        print(f"player {list1[3]} is win")
        close_and_sleep()

    elif list1[6] == list1[7] == list1[8]:
        print(f"player {list1[6]} is win")
        close_and_sleep()

    elif list1[0] == list1[4] == list1[8]:
        print(f"player {list1[0]} is win")
        close_and_sleep()

    elif list1[6] == list1[4] == list1[2]:
        print(f"player {list1[6]} is win")
        close_and_sleep()

    elif list1[0] == list1[3] == list1[6]:
        print(f"player {list1[0]} is win")
        close_and_sleep()

    elif list1[1] == list1[7] == list1[4]:
        print(f"player {list1[1]} is win")
        close_and_sleep()

    elif list1[2] == list1[5] == list1[8]:
        print(f"player {list1[2]} is win")
        close_and_sleep()

    else :
        return False


#Function for check the Draw
def check_draw():
    a = 0
    for n in range(9):
        if n+1 in list1:
            pass
        else:
            a += 1

    if a == 9:
        if check_winner():
            pass
        else:
            print("Game over 'Draw'")
            close_and_sleep()
    


# Function for check if the input is eror
def check_input(n):
    input_xo_list = ['x', 'X', 'o', 'O']

    if n in input_xo_list:
        return False

    else:
        return True


def close_and_sleep():
    time.sleep(5)
    sys.exit()

a = "X"
b = "O"

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcom to 'X O' game")


# the body of the game
body_of_game = f'''
        {list1[0]}   |   {list1[1]}   |  {list1[2]}

        {list1[3]}   |   {list1[4]}   |  {list1[5]}

        {list1[6]}   |   {list1[7]}   |  {list1[8]}
        '''

print(body_of_game)


# a big while true loop
while True:

    # a small for loop with 3 traise because if user enter wrong number
    for n in range(3):

        # the choise of user
        choise1 = input("X -> Enter your choise: ").strip()

        # try if choise is integer number or no
        try:
            choise1 = int(choise1)
            choise1 -= 1

        except:
            print("input Eror")
            continue

        if check_input(choise1):
            pass
        else:
            print("input Eror")
            close_and_sleep()


        if choise1 + 1 in list1:

            list1[choise1] = a


            # drew the body of game again to save the changes
            body_of_game = f'''
        {list1[0]}   |   {list1[1]}   |  {list1[2]}

        {list1[3]}   |   {list1[4]}   |  {list1[5]}

        {list1[6]}   |   {list1[7]}   |  {list1[8]}
        '''

            print(body_of_game)

            check_winner()
            check_draw()

            break

        else:

            continue

    #if the user input 3 wrong input
    else:
        print("your Chances is ended")
        close_and_sleep()

#______________________________________________________________________________

    # a big while true loop
    for n in range(3):

        # a small for loop with 3 traise because if user enter wrong number
        choise2 = input("O -> Enter your choise: ").strip()


        # try if choise is integer number or no
        try:
            choise2 = int(choise2)
            choise2 -= 1

        except:
            print("input Eror")
            continue


        if check_input(choise2):
            pass
        else:
            print("input Eror")
            close_and_sleep()


        if choise2 + 1 in list1:
            list1[choise2] = b


            # drew the body of game again to save the changes
            body_of_game = f'''
        {list1[0]}   |   {list1[1]}   |  {list1[2]}

        {list1[3]}   |   {list1[4]}   |  {list1[5]}

        {list1[6]}   |   {list1[7]}   |  {list1[8]}
        '''

            print(body_of_game)

            check_winner()
            check_draw()

            break

        else:

            continue


    #if the user input 3 wrong input
    else:
        print("your Chances is ended")
        close_and_sleep()
