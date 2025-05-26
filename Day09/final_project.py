'''Blind auction program'''
import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_bid(bids, name, bid):
    bids[name]= bid

def continu_or_not():
    yes_or_no= input("Are there any other bidders? 'yes' or 'no'? ")
    if yes_or_no == 'yes':
        return True
    elif yes_or_no == 'no':
        return False
        
def blind_auction():
    bids={}
    continue_bid= True
    max_bid=0
    winner=''
    print(" Welcome to the secret auction program.")
    while continue_bid:
        name= input("What is your name? ")
        bid= float(input("What is your bid? "))
        add_bid(bids, name, bid)
        if not continu_or_not():
            continue_bid= False
        clear()

    for key in bids:
        if bids[key]> max_bid:
            max_bid = bids[key]
            winner= key
    print(f"The winner is {winner} with a bid of ${max_bid}") 

blind_auction()
        
