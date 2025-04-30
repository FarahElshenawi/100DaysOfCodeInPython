import os 

bids={}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the secret auction program.")
while True:
    name= input("What is your name? ")
    bid= float(input("What is your bid? "))
    bids[name]= bid
    more= input("Are there any other bidders? 'yes' or 'no'? ").lower()
    clear()
    if more == 'no':
        break

winner= max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}") 
