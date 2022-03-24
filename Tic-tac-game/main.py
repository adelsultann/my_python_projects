import random


# Tic-Tac-Toe Game


class TickTackToe:
    def __init__(self):
        self.board = []

    def create_board(self, board):
        print("\n" * 100)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    # choose a random player to start playing
    def choose_first(self):
        flip = random.randint(0, 1)
        if flip == 0:
            return "Player 1"
        else:
            return "Player 2"

    # input for players either X or O
    def player_input(self):
        marker = " "
        while not (marker == "X" or marker == "O"):
            marker = input('Choose X or O: ').upper()
        if marker == "X":

            return ("X", "O")
        else:
            return ("O", "X")

    def place_marker(self, board, marker, position):
        board[position] = marker

    def win_check(self, board, mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
                (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
                (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
                (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
                (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
                (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
                (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
                (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

    def full_board_check(self, board):
        for i in range(1, 10):
            if self.space_check(board, i):
                return False

    def space_check(self, board, position):

        return board[position] == ' '

    def player_choice(self, board):
        position = 0
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.space_check(board, position):
            position = int(input('Enter a number from 1 to 9: '))
        return position

    def replay(self):

        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


game = TickTackToe()

while True:
    the_board = [" "] * 10
    player_1, player2 = game.player_input()
    turn = game.choose_first()
    print(turn, "Will go first")
    play_game = input("Are you ready to play?Enter Yes or No: ")
    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            game.create_board(the_board)
            position = game.player_choice(the_board)
            game.place_marker(the_board, player_1, position)
            if game.win_check(the_board, player_1):
                game.create_board(the_board)
                print("You have won")
                game_on = False
            else:
                if game.full_board_check(the_board):
                    game.create_board(the_board)
                    print("the game is draw")
                    game_on = False

                else:
                    turn = "Player 2"
        else:
            game.create_board(the_board)
            position = game.player_choice(the_board)
            game.place_marker(the_board, player2, position)
            if game.win_check(the_board, player2):
                game.create_board(the_board)
                print("You have won")
                game_on = False

            else:
                if game.full_board_check(the_board):
                    game.create_board(the_board)
                    print("the game is draw")
                    break
                else:
                    turn = "Player 1"

    if not game.replay():
        break