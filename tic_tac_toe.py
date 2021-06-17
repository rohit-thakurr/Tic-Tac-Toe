# Tic-Tac-Toe game

#Print Board

print("Board looks like this, with the position mention here")
print("  7  " + "   |   " + "  8  " + "   |   " + "  9  ")
print("--------|" + "-----------|" + "---------")
print("  4  " + "   |   " + "  5  " + "   |   " + "  6  ")
print("--------|" + "-----------|" + "---------")
print("  1  " + "   |   " + "  2  " + "   |   " + "  3  ")
print("--------|" + "-----------|" + "---------")


def display_board(board):

    print("  "+board[6]+"  "+"   |   "+"  "+board[7]+"   |   "+board[8])
    print("--------|"+"---------|"+"-------")
    print("  "+board[3]+"  "+"   |   "+"  "+board[4]+"   |   "+ board[5])
    print("--------|"+"---------|"+"-------")
    print("  "+board[0]+"  "+"   |   "+"  "+board[1]+"   |   "+ board[2])
    print("--------|"+"---------|"+"-------")

print("\n"*4)

board1=[" "]*10

def choose_your_marker(player1="a",player2="b"):

    while player1 != "X" and player1 != "O":
        print(" Player1 choose between X or O")
        name=input()
        player1=name.capitalize()

    if player1=="X":
        player2="O"
    else:
        player2="X"

    return (player1,player2)


(player_one_marker,player_two_marker)=choose_your_marker()
print("So Player1 marker is",player_one_marker)
print("And Player2 marker is",player_two_marker)

# Winning Possibilities

def result_of_game(list1,player_marker):
    if list1[0]==player_marker and list1[1]==player_marker and list1[2]==player_marker:
        return "Win"
    elif list1[3]==player_marker and list1[4]==player_marker and list1[5]==player_marker:
        return "Win"
    elif list1[6]==player_marker and list1[7]==player_marker and list1[8]==player_marker:
        return "Win"
    elif list1[0]==player_marker and list1[3]==player_marker and list1[6]==player_marker:
        return "Win"
    elif list1[1]==player_marker and list1[4]==player_marker and list1[7]==player_marker:
        return "Win"
    elif list1[2]==player_marker and list1[5]==player_marker and list1[8]==player_marker:
        return "Win"
    elif list1[0]==player_marker and list1[4]==player_marker and list1[8]==player_marker:
        return "Win"
    elif list1[2]==player_marker and list1[4]==player_marker and list1[6]==player_marker:
        return "Win"
    else:
        return "Continue"


def game(board,player1,player2):
    num=1
    marker=""
    x=True
    while x:
        if num%2==1:
            marker=player1
        else:
            marker=player2

        if marker=="X":
            print("Player1 enter your position:")
        else:
            print("Player2 enter your position:")

        marker_position = int(input())
        print("\n" * 25)
        board[marker_position - 1] = marker
        display_board(board)

        result=result_of_game(board,marker)
        if result=="Win":
            if num % 2 == 1:
                print("Player1 Win The Game")
                x=False
            else:
                print("Player2 Win The Game")
                x=False

        empty_string=""
        k=9
        for item in board:
            if item==empty_string:
                k=k-1

            if k==0:
                print("End of The Game, There is no winner")
                x=False

        num=num+1

game(board1,player_one_marker,player_two_marker)








