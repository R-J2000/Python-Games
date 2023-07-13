import math
import random


class Player():
    def __init__(self, letter):
        # Letter is x or o -- it is a mark correspnding of the player tic-tac-toe symbol
        self.letter = letter
    
    # Method to get a player their next move given a game
    def get_move(self, game):
        pass


# Using inheritance, set up another class for random computer player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

# Using inheritance, set up another class for human player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # We're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not , then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
    

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter # This is you!
        other_player = 'O' if player == 'X' else 'X' # This var. will take on the value of you and your opponent during alternating recursion

        # First we want to check if the previous move is a winner: This is our Base Cases!
        if state.current_winner == other_player: # Other player is merely a placeholder here
            # We need position and minimax score to supply the algorithim with relevant data. 
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        # Provides minimax score for draw
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        # Initialize a dictionary to keep track of the best route
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # When the score needs to be maximized
        else:
            best = {'position': None, 'score': math.inf} # When the score needs to be minimized

        # Iterate over all possible moves in Depth First Search
        for possible_move in state.available_moves():
            # Step 1: Make and test move
            state.make_move(possible_move, player)
            # Step 2: Recurse using minimax to stimulate game after move
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move. NOTE: minimax is called with "other_player"

            # Step 3: Undo move; Clean up for next iteration
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
    
            # Step 4: Update dict. if a new best score is found
            if player == max_player:  
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

        







