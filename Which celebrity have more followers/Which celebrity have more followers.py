#For the game, two random options would be provided for which you have to guess
#the one with more followers.
#You can keep on playing untill unless you don't give a wrong answer.
#You can see

from game_data import data
import random



#Choosing a random value from our data set.
#if both account values are similar, we will use random.choice again to make sure
#that both values are distinct.

    
def format(account):
    
    '''Formating the account data into a printable form.'''
    
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

    
def get_random_account():
   
    """Get data from random account"""
  
    return random.choice(data)   


def check_answer(guess, a_followers, b_followers):
    
  """Checks followers against user's guess and returns True if they got it right.
     Or False if they got it wrong.""" 
     
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def playgame():

  count = 0
  game_should_continue = True
  account_A = get_random_account()
  account_B = get_random_account()
  
  while game_should_continue:
    account_A = account_B
    account_B = get_random_account()
    
    while account_A == account_B:
      account_B = get_random_account()
    print(f"\nOption A: {format(account_A)}.")
    print(f"Option B: {format(account_B)}.")
  
    guess = input("\nWho has more followers? Type 'A' or 'B':").lower()
    
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
      count += 1
      print(f"\nYou're right! Current score: {count}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {count}")
      
playgame()