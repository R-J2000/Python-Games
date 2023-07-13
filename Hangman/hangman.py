import random
from words import words
from hangman_visuals import lives_visual_dict
import string

# Gets words without '-' and ' ' (dashes or empty spaces)
def get_valid_word(words):

    # Choose random word from set words in file words
    word = random.choice(words)
    # Check validity as described above def
    while (' ' in word) or ('-' in word):
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has already guessed

    lives = 6 # Number of attempts remaining before the player loses

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] # This line is absolutely beautiful!
        print ('Current word: ', ' '.join(word_list))

        user_letter = input('What is your next letter?: ').upper()

        # Check if the user guess is correct or not. Modify tracking variables correspndingly
        if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)

                else:
                     lives = lives - 1 # takes away a life if wrong
                     print('Letter is not in word.')

        # Check if the letter was already selected
        elif user_letter in used_letters:
            print('Sorry, already used. Please pick another letter.')
        
        # Deal with letter that are not legitimate
        else:
            print('Invalid character. Please pick another letter')

        print(lives_visual_dict[lives])

    
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

hangman()

