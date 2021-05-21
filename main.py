from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bids = {}
choice = True
while(choice):
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if other == "no":
    choice = False
  clear()
  
max_bid = max(bids, key=bids.get)
print(f"The winner is {max_bid} with a bid of ${bids[max_bid]}")