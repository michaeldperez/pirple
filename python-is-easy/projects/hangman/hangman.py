from getpass import getpass
from hangman_player import HangmanPlayer
from hangman_word import HangmanWord
from hangman_figure import HangmanFigure

class Hangman:
    def __init__(self):
        self.player_one = HangmanPlayer(1)
        self.player_two = HangmanPlayer(2)
        self.hangman_figure = HangmanFigure()
        self.word = None
        self.incorrect_guess_limit = 6
        self.game_is_being_played = True
        self.guessed_letters = []
    
    def set_incorrect_guess_limit(self, limit):
        self.incorrect_guess_limit = limit
    
    def check_incorrect_guess_limit(self, current_number_of_incorrect_guesses):
        return (False, True)[current_number_of_incorrect_guesses >= self.incorrect_guess_limit]

    def set_word(self, hangman_word, word):
        self.word = hangman_word(word)
    
    def add_guessed_letter(self, letter):
        self.guessed_letters.append(letter)

    def start(self):
        print("Welcome to Hangman.")
        selected_word = getpass("Player One please choose a word: ").lower()
        self.set_word(HangmanWord, selected_word)

        while self.game_is_being_played:
            print(f"Guessed letters: {self.guessed_letters}\n\n")
            print(f"{self.word.obfuscated_word}\n\n")
            self.hangman_figure.render()

            guessed_letter = input("Player Two please guess a letter: ")

            if guessed_letter in self.guessed_letters:
                print(f'You already guessed {guessed_letter}.')
                continue

            self.add_guessed_letter(guessed_letter)
            letter_exists, is_discovered = self.word.check(guessed_letter)

            if is_discovered:
                self.game_is_being_played = False
                print("Player Two Wins!")
            else:
                if letter_exists:
                    print(f"Correct guess! {guessed_letter} is in word")
                else:
                    print(f"Incorrect guess. '{guessed_letter}' is not in word.")
                    self.player_two.increment_incorrect_guesses()
                    number_of_incorrect_guesses = self.player_two.number_of_incorrect_guesses()
                    self.hangman_figure.render_next()
                    guess_limit_reached = self.check_incorrect_guess_limit(number_of_incorrect_guesses)
                    if guess_limit_reached:
                        self.game_is_being_played = False
                        print("Player Two loses")

        print(f"The correct word was \"{self.word.word}.\"")

if __name__ == "__main__":
    game = Hangman()
    game.start()