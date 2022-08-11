from replit import clear
from art import logo

bids = {}  # only for use with additional functionality, otherwise not really necessary

while True:
    print(logo)
    name = input("what is your name/email? ").lower()
    bid = int(input('Please enter your bid: $'))
    other_bids = input("Are there other bidders in the room? Y/N ").upper()
    bids[name] = bid
    highest_bidder = {'name': '', 'bid': 0}
    if bid >= highest_bidder['bid']:
        highest_bidder['name'] = name
        highest_bidder['bid'] = bid
    if other_bids == 'Y':
        clear()
    else:
        # highest_bidder['bid'] = f"${highest_bidder['bid']}"
        # print(highest_bidder)
        print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}")
        break
