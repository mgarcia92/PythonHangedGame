import random

class HangmanGame:
   def __init__(self):
       self.list_words = []
       self.hidden_word = []
       self.idx_board = 0
       self.idx_word = 0
       self.tries = 0
       self.current_letter = ''
       self.word = ''
       self.correct_letters = []
       self.images =  ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

   def random_word(self):
        index = random.randint(0, len(self.list_words) - 1)
        return self.list_words[index]

   def read_data(self):
    try:
      with open('./data.txt', encoding="utf-8") as f:
        for word in f:
          self.list_words.append(word.replace('\n',''))
    except FileNotFoundError:
      print("File Not Found")

   def show_board(self,askLetter = True):
       print(self.images[self.tries])
       print('')
       print(self.hidden_word)
       if askLetter == True:
         self.current_letter = input('Write a letter: ')

   def start_game(self):
       print("WELCOME TO HANGED GAME IN PYTHON")
       self.read_data()
       self.word = self.random_word()
       word_len = len(self.word)
       self.hidden_word = ['-' for x in range(0, len(self.word))]
       self.correct_letters = [False for x in range(0, len(self.word))]
       self.show_board()
       while True:
         if self.is_match_letter(letter = self.current_letter) == True:
            self.hidden_word[self.idx_word] = self.current_letter
            self.correct_letters[self.idx_word] = True
            if len(list(filter(lambda x: x == True,self.correct_letters))) == word_len:
                self.show_board( askLetter =  False)
                print("Your are the Winner Congratulation")
                break;
            else:
                self.show_board()
         else:
            self.tries += 1
            if self.tries == 7:
                self.show_board()
                print("Game Over, the word is {}".format(self.word))
                break
            else:
                self.show_board()

   def is_match_letter(self,letter):
    index = 0
    matched = False
    for idx in self.word:
        if idx.lower() == letter.lower() and self.correct_letters[index] == False:
           self.idx_word = index
           matched = True
        index += 1

    return matched

if __name__ == '__main__':
    game = HangmanGame()
    game.start_game()


       

    









                      
                
                    
                


   
