from random_words import RandomWords

class Game(object):
    def __init__(self):
        self.communication = Communication()
        self.game_logic = GameLogic()
        self.draw = Draw()
        self.start()

        def start(self):
            self.random_word = self.game_logic.create_randomword()
            self.guessed_word = ["_" for i in range (len(self.random_word)))]
            self.guess_number = 0
            self.game_running = True
            self.game()

        def game(self):
            while self.game_running:
                self.guessed_letter = self.communication.get_letter(self.guessed_word)
                self.game_running = False
        


class Communication(object):
    def get_letter(self):
        print(guessed_word)
        return input("Guess a letter: ")

class GameLogic(object):
    def __init__(self):
        self.rdm_wrd = RandomWords()

        def create_randomword(self):
            return self.rdm_wrd.random_word()

class Draw(object):
    pass

game = Game()
