import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe():
    
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to represent a 3x3 board
        self.current_winner = None # keep track of winner!


    def print_board(self):
        # EXPLAIN LOGIC OF BELOW LOOP
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # Iterates over each row: indicies [0,1,2] [3,4,6] [7,8,9]
            print('| ' + ' | '.join(row) + ' |') # Join rows where the separator is ' | '. Each iteration will print | 0 | 1 | 2 |


    @staticmethod # Static Method that doesn't relate to any specific board
    def print_board_nums():
        # This is just getting the rows 0 | 1 | 2. This tells us what number correspnds to what box.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    # EXPLAIN LOGIC OF BELOW METHOD
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
        # moves = []
        # for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ') 
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # Check for Win Condition
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    

    
    def winner(self, square, letter):
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        # print('row', row)
        if all([spot == letter for spot in row]):
            return True
        
        # Check Coloumn
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([spot == letter for spot in column]):
            return True
        
        # Check Diagonals
        # But only if the sqaure is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Left to right diagonal
            # print('diag1', diagonal1)
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # Right to left diagonal
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
            
        # If all fails
        return False
    

            

def play(game, x_player, o_player, print_game=True):
    # Returns the winner of the game (the letter)! or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # Starting Letter
    # Iterate while the game still has empty sqaures
    # (we don't have to worry about winner because we'll just return that
    # which break the loop)
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Let's define a function to make a move!
        if game.make_move(square, letter):

            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # Just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        # Tiny Break to make things a little easier to read
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)