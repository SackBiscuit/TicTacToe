
#board -----done
#writing on board -----done
#switch turn -----done
#check win row - clome digno ----done
#input error catch done
# check for tie done
#check if the space is used done

#CPU

# Global ----
turn = ''
shown_turn = ''
winner= ''
check_if_win = False
check_if_tie = False
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def Play_game():

    while check_if_win == False or check_if_tie == False:
        check_trun = False
        print_board = board[0] + " | " + board[1] + " | " + board[2] +"\n"+\
                      board[3] + " | " + board[4] + " | " + board[5] +"\n"+\
                      board[6] + " | " + board[7] + " | " + board[8]

        print(print_board)



        Check_Winner()
        check_tie()

        if shown_turn == 'X' or 'O' and shown_turn != '' and check_if_win == False:
            print("It's " + shown_turn+ " turn")
            
        if winner == 'X' or 'O' and check_if_win == True:
            print("Yay " + winner + " won.")
            break
        elif check_if_tie == True:
            print("Tie :(")
            break

        Player = input("Enter a number between 1 to 9")

        while Player not in ["1","2","3","4","5","6","7","8","9"]:
                Player= input("only numbers between 1 to 9")

        while check_trun ==False:
            if board[int(Player) -1 ] == '-':
                check_trun = True
                board[int(Player) - 1] = Switch_Turn(turn)
            else:
                print("Used Space try again")
                break


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


def check_tie():
    global check_if_tie
    for i in board:
        if i == '-':
            return

    check_if_tie = True


Play_game()