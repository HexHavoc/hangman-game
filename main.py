from hangman_art import *

class Hangman:
    def __init__(self):
       self.win_case = False 
       self.chance = 6 
       self.hangman_index = 1
       print("Welcome to Hangman Game\n")
       print(f"You have {self.chance} chances so play carefully!!! :)\n")
       print("\n")
       print("Lets Start!!!\n") 
       print(hangman_pics[0])
       print()
            
    
    def word_pick(self):
        self.word = "anirudh"
        self.word_hidden = ""
        for i in self.word:
            self.word_hidden += '-'
        
        self.word_hidden_list = list(self.word_hidden)
        self.display_word = self.word_hidden
        
           
    
    def word_prompt_check(self):
        print(f"The word is {self.display_word}\n")
        
        while True:
            self.guess_word = input("Enter your guess: > ")
            
            if(len(self.guess_word) > 1):
                if self.guess_word in self.word:
                    for i in self.guess_word:
                            index = self.word.index(i)
                            self.word_hidden_list[index] = i
                            self.word_hidden = ''.join(self.word_hidden_list)
                            
                            
                print(self.word_hidden)
            
            # this else deals with the case of if the user enters only one letter
            
            else:
                if self.guess_word in self.word:
                    print("Congrats your guess is in the word!\n")
                    for i in self.word:
                        if(i == self.guess_word):
                            index = self.word.index(i)
                            self.word_hidden_list[index] = self.guess_word
                            self.word_hidden = ''.join(self.word_hidden_list)
                            if(self.word_hidden == self.word):
                                self.win_case = True
                                print("HOORAY YOU DID IT YOU GUESSED THE WORD!!!!!\n")
                                print(f"The word is {self.word}")
                                break
                    
                    if(self.win_case):        
                        play_choice = input("Wanna play again?(Y/N): > ").upper()
                        if(play_choice == 'Y'):
                            print('\n')
                            print('\n')
                            print(f"The word is {self.display_word}\n")
                            continue
                        
                        else:
                            break
                    


                else:
                    self.chance -= 1
                    print("Your guess is not in the word :( \n")
                    print(hangman_pics[self.hangman_index])
                    print("\n")
                    if(self.chance == 0):
                        print("Good try but your chances reached 0 better luck next time :) \n")
                        print(f"The word you were trying to guess was {self.word} \n")
                        
                        play_choice = input("Wanna play again?(Y/N): > ").upper()
                        if(play_choice == 'Y'):
                            print('\n')
                            print('\n')
                            print(f"The word is {self.display_word}\n")
                            continue
                        
                        else:
                            break
                        
                    print(f"You have {self.chance} chances left :) \n")
                    self.hangman_index += 1
                    
                
                
                print(f"The word is {self.word_hidden}\n")
            
            
    def call_everything(self):
        self.word_pick()
        self.word_prompt_check()           
                
    
man = Hangman()

man.call_everything()