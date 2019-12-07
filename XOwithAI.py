import random
import time
# Global ----

turn = ''
shown_turn = ''
winner= ''
check_if_win = False
check_if_tie = False
AI_win = False
board_copy = []
Remaining_plays = []
corners = []
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def Play_game():

    global turn
    while check_if_win == False or check_if_tie == False:
        check_trun = False
        print_board = board[0] + " | " + board[1] + " | " + board[2] +"\n"+\
                      board[3] + " | " + board[4] + " | " + board[5] +"\n"+\
                      board[6] + " | " + board[7] + " | " + board[8]

        print(print_board)

        CPU1 = 0
        cpu_play= 0
        Check_Winner()
        check_tie()


        if winner == 'X' or 'O' and check_if_win == True:
            print("Yay " + winner + " won.")
            break
        elif check_if_tie == True:
            print("Tie :(")
            break
        if shown_turn == 'X' or shown_turn == '':

            Player = input("Enter a number between 1 to 9")
            while Player not in ["1","2","3","4","5","6","7","8","9"]:
                    Player= input("only numbers between 1 to 9")

            while check_trun == False:
                 if board[int(Player) -1 ] == '-':
                     check_trun = True
                     board[int(Player) - 1] = Switch_Turn(turn)
                 else:
                     print("Used Space try again")
                     break

        #AI turn
        elif shown_turn == 'O' and check_if_win == False:
            time.sleep(0.3)
            CPU1 = biscuit(cpu_play)
            AI_play = CPU1 +1
            print("AI played on "+str(AI_play) +" slot")

            board[int(CPU1)] = Switch_Turn(turn)


def biscuit(play):

    global corners
    global Remaining_plays
    board_copy = board[:]
    Remaining_plays = []
    # check for posible losing spot
    ai_play = 0
    loop_number = 0
    for xo in ['O', 'X']:
        loop_number = 0
        board_copy = board[:]

        for i in board_copy:
            if board_copy[loop_number] == '-':
                Remaining_plays.append(loop_number)
            loop_number += 1

        for i in Remaining_plays:
            board_copy = board[:]
            board_copy[i] = xo
            if AI_check_for_win(board_copy):
                ai_play = i
                Remaining_plays = []
                return ai_play

    corners = []
    for i in [0, 2, 6, 8]:
        if board[i] == '-':
            corners.append(i)
        if len(corners) > 0:
            return random.choice(corners)

    if board[4] == '-':
        return 4

    Remaining_plays= []
    loop_number = 0
    for i in board:
        if board[loop_number] == '-':
            Remaining_plays.append(loop_number)
        loop_number += 1
    for i in Remaining_plays:
        if board[i] == '-':
            return i

def Switch_Turn(turn1):
    global turn
    global shown_turn
    if turn1 == 'X':
        turn = 'O'
        shown_turn = 'X'
        return 'O'
    else:
        turn = 'X'
        shown_turn = 'O'
        return 'X'


def Check_Winner():
    global winner
    global check_if_win
    #Rows --
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        check_if_win = True
        return
    elif board[3] == board[4] == board[5] != "-":
        winner= board[3]
        check_if_win = True
        return
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        check_if_win = True
        return
    #Col --
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        check_if_win = True
        return
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        check_if_win = True
        return
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        check_if_win = True
        return
    #digno --
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        check_if_win = True
        return
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        check_if_win = True
        return
    else:
        return


def AI_check_for_win(c_board):

    #Rows --
    if c_board[0] == c_board[1] == c_board[2] != "-" :
        return True
    elif c_board[3] == c_board[4] == c_board[5] != "-" :
        return True
    elif c_board[6] == c_board[7] == c_board[8] != "-" :
        return True
    #Col --
    if c_board[0] == c_board[3] == c_board[6] != "-" :
        return True
    elif c_board[1] == c_board[4] == c_board[7] != "-":
        return True
    elif c_board[2] == c_board[5] == c_board[8] != "-":
        return True
    #digno --
    if c_board[0] == c_board[4] == c_board[8] != "-":
        return True
    elif c_board[2] == c_board[4] == c_board[6] != "-":
        return True
    else:
        return False


def check_tie():
    global check_if_tie
    for i in board:
        if i == '-':
            return

    check_if_tie = True


Play_game()