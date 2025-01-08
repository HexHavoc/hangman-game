from hangman_art import *
from wordbank import *
from wordbank import *
import os

class Hangman:
    def __init__(self):
       self.chance = 6 
       self.hangman_index = 1
       print("Welcome to Hangman Game\n")
       print(f"You have {self.chance} chances so play carefully!!! :)\n")
       print("\n")
       print("Lets Start!!!\n") 
       print(hangman_pics[0])
       print()
            
    
    def word_pick(self):
        self.word = random_word
        print(self.word)
        self.word_hidden = ""
        for i in self.word:
            self.word_hidden += '-'
        
        self.word_hidden_list = list(self.word_hidden)

    
    def duplicate_check(self,guess_word,hidden_word):
        if(guess_word in hidden_word):
            print("You know this guess was already in the word try something else :)")
            return True
    
    
           
    
    def word_prompt_check(self):
        
        while True:
            print(f"The word is {self.word_hidden}\n")
            self.guess_word = input("Enter your guess: > ")
            
            
            # this if statement deals with when user enters more than 1 character
            
            if(len(self.guess_word) > 1):
                if(self.duplicate_check(self.guess_word,self.word_hidden)):
                    continue

                if self.guess_word in self.word:
                    print("Congrats your guess is in the word!\n")
                    for i in self.guess_word:
                            index = self.word.index(i)
                            self.word_hidden_list[index] = i
                            self.word_hidden = ''.join(self.word_hidden_list)
                            
                    
                    if(self.word_hidden == self.word):
                         print("HOORAY YOU DID IT YOU GUESSED THE WORD!!!!!\n")
                         print(f"The word is {self.word}\n")
                         print()
                         play_choice = input("Wanna play again?(y/n): > ").lower()
                         if(play_choice == 'y'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            self.__init__()
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
                        
                        play_choice = input("Wanna play again?(y/n): > ").lower()
                        if(play_choice == 'y'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            self.__init__()
                            continue
                        
                        else:
                            break

                    if(self.chance == 1):
                        print(f"You only have {self.chance} more chance left :) \n")

                    else:
                        print(f"You have {self.chance} chances left :) \n")
                    
                    self.hangman_index += 1
                


                    
            # this else deals with the case of if the user enters only one letter
            
            else:
                if(self.duplicate_check(self.guess_word,self.word_hidden)):
                    continue
                
                if self.guess_word in self.word:
                    print("Congrats your guess is in the word!\n")
                    for i in self.word:
                        if(i == self.guess_word):
                            index = self.word.index(i)
                            self.word_hidden_list[index] = self.guess_word
                            self.word_hidden = ''.join(self.word_hidden_list)
                    
                    if(self.word_hidden == self.word):
                                
                                print("HOORAY YOU DID IT YOU GUESSED THE WORD!!!!!\n")
                                print(f"The word is {self.word}\n")
                                print()
                                play_choice = input("Wanna play again?(y/n): > ").lower()
                                if(play_choice == 'y'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    self.__init__()
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
                        
                        play_choice = input("Wanna play again?(y/n): > ").lower()
                        if(play_choice == 'y'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            self.__init__()
                            continue
                        
                        else:
                            break
                        
                    if(self.chance == 1):
                        print(f"You only have {self.chance} more chance left :) \n")

                    else:
                        print(f"You have {self.chance} chances left :) \n")
                    
                    self.hangman_index += 1
                    
            
            
    def call_everything(self):
        self.word_pick()
        self.word_prompt_check()           
                
    
man = Hangman()

man.call_everything()