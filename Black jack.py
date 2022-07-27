############### Blackjacke Rules ###############################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

import random

#Will create a deal_card function which will ensure that dealer and user have 2 randomly selected cards.
#11 number is the Ace.

def deal_card(): 
    
    """Returns a random card from deck"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
    
#Calculating the score.

def calculate_cards_score (cards):
    
    """Returns the sum of scores using the cards's list"""
   
    #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10 point card). 
    #0 will represent a blackjack in our game.  
    if sum(cards)==21 and len(cards) == 2:
        return 0
    
    #If the score is already over 21, remove the 11 and replace it with a 1.
    #Ace can have either value 1 or 11.
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Comparing the scores.

def compare(user_s,dealer_s):  
    
                               """If both of you went over 21, you lose.      
                                  If the dealer and user both have the same score, then it's a draw.
                                  If the dealer has a blackjack, then the user loses. 
                                  If the user has a blackjack, then the user wins. 
                                  If the user_score is over 21, then the user loses. 
                                  If the dealer's score is over 21, then the dealer loses. 
                                  If none of the above, then the player with the highest score wins."""
   
    if user_s >21 and dealer_s >21:
        return "\nYou went over 21, YOU LOSE"
    if user_s==dealer_s:
        return "\nDRAW ;)"                
    elif dealer_s==0:
        return "\nYou LOST, dealer has a blackjack"
    elif user_s==0:
        return "\nYOU WIN ! You hit a black jack"
    elif user_s >21:
        return "\nYOU LOSE. Your score is over 21"
    elif dealer_s >21:
        return "\nYOU WIN ! Dealer score is over 21"
    elif user_s>dealer_s:
        return "\nYOU WIN !"
    else:
        return "\nYOU LOST HAAHAHAH"  

def game():
    
    user_cards=[]
    dealer_cards=[]
    game_over=False
    
    #Randomly choosing 2 cards for user and dealer.
      
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
          
        #If the dealer or the user has a blackjack or if the user's score is over 21, then the game ends.
    
    while not game_over:    
        user_s=calculate_cards_score(user_cards)
        dealer_s=calculate_cards_score(dealer_cards)
        print(f"\nYour cards are: {user_cards}, current score: {user_s}")
        print(f"Dealer's first card: {dealer_cards[0]}\n")
        
        if user_s==0 or dealer_s==0 or user_s>21:
            game_over=True
        else:
            
            #If the game is still not over, ask the user if they want to draw another card.
            #If yes, then add a card to their list.
            #If no, then the game has ended.
            
            deal= input("Type 'y' to call for another card, type 'n' to pass: ")
            if deal =='y':
                user_cards.append(deal_card())
            else:
                game_over=True    
    
    print(f"User cards = {user_cards}")
        
    #When user is done picking the cards, its dealer's turn.
    #Dealer will keep on choosing the cards until unless its score is less than 17.          
    
    while dealer_s !=0 and dealer_s <17:
        dealer_cards.append(deal_card())
        dealer_s=calculate_cards_score(dealer_cards)
    
    #Final results.    
    
    print(f"Your final hand: {user_cards}, final score: {user_s}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_s}")
    
    print(compare(user_s, dealer_s))

while input("\nDo you want to play black jack ? Type 'y' or 'n': ")=="y":
    game()