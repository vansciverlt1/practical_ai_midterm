import random


word_list = [
    "python",
    "hangman",
    "computer",
    "programming",
    "keyboard",
    "elephant",
    "calendar",
    "sunshine",
    "mountain",
    "basketball",
    "orchestra",
    "universe",
    "chemistry",
    "adventure"
]




def select_random_word():
    return random.choice(word_list)




def initialize_game_state(word):
    return {"word": word,
        "guessed_letters": [],
        "word_completion": "_" * len(word),
        "tries_remaining": 6 }




HANGMAN_STAGES = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''
]




def display_game_state(game_state):
    stage = HANGMAN_STAGES[6 - game_state["tries_remaining"]]
    print(stage)
   
    word_completion = ' '.join(game_state["word_completion"])
    print(f"Word: {word_completion}")
   
    guessed_letters = ' '.join(game_state["guessed_letters"])
    print(f"Guessed letters: {guessed_letters}")
   
    print(f"Tries remaining: {game_state['tries_remaining']}")


def guess_a_letter(game_state):
    while True:
        letter_guess = input("Guess a letter: ").lower()  
        if len(letter_guess) == 1 and letter_guess.isalpha() and letter_guess not in game_state['guessed_letters']:
            return letter_guess
        print("Make sure you have written only one letter.")


def update_game(game_state, guessed_letter):
    game_state['guessed_letters'].append(guessed_letter)
   
    if guessed_letter in game_state['word']:
        new_completion = list(game_state['word_completion'])
       
        for i, letter in enumerate(game_state['word']):
            if letter == guessed_letter:
                new_completion[i] = guessed_letter
       
        game_state['word_completion'] = ''.join(new_completion)
        return True
    else:
        game_state['tries_remaining'] -= 1
        return False




def game_over(game_state):
    return '_' not in game_state['word_completion'] or game_state['tries_remaining'] == 0




def player_won(game_state):
    return game_state['word_completion'] == game_state['word']


def main_game():
    word = select_random_word()
    game_state = initialize_game_state(word)
    print("Let's start a game of Hangman!")
    display_game_state(game_state)


    while not game_over(game_state):
        guessed_letter = guess_a_letter(game_state)
        update_game(game_state, guessed_letter)
        display_game_state(game_state)
       
    if player_won(game_state):
        print("You won! Nice!")
    else:
        print(f"I win! The word was: {game_state['word']}")


if __name__ == "__main__":
    print("Are you ready to play a game of Hangman?")
   
    while True:
        main_game()
        another_game = input("Would you like to play again? (yes/no): ").lower()
        if another_game != 'yes':
            print("Thanks for playing!")
            break
