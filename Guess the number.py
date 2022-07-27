import random

num=random.randint(1, 100)
print("Welcome to the 'NUMBER GUESSING GAME'")
print("\nI am thinking of a number between 1 and 100 and to win the game you have to guess the number.\n")
EASY_TURNS=10
HARD_TURNS=5

def game():
    
    def check(guess,num,turns):
        
        """"Checks answer against guess. Returns number of turns remaining """
        
        if num>guess:
            print("Your guess is too low")
            return turns-1
        elif num<guess :
            print("Your guess is too high")
            return turns-1
        else:
            print(f"\n\tYou got it, answer is {num}")
            
    def difficulty():
        
        """"Determines the difficulty of the game """
        
        level=input("Choose a difficulty. Type 'easy'or 'hard': ")     
        if level=="easy":
            return EASY_TURNS
        else:
            return HARD_TURNS
            
    turns=difficulty()  
 
    guess=0
    while guess!=num:
        print(f"You have {turns} attempts.")        
        guess=int(input("\nMake a guess: "))
        turns=check(guess,num,turns)
        if turns==0:
            st=print("\tYOU LOST !!!")
            return st 
        elif num !=guess:
            print("\n\tTry again")

game()      
       








