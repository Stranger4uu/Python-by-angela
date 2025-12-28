logo = r"""
        ___________
       \         /
        )_______(
        |"""""""|_.-._,.---------.,_.-._
        |       | | |               | | ''-.
        |       |_| |_             _| |_..-'
        |_______| '-' `'---------'` '-'
        )"""""""(
       /_________\
       `'-------'`
     .-------------.
 /_______________\
"""

print(logo)
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0 
    for bidder in bidding_dictionary:
        Bid_amount = bidding_dictionary[bidder]
        if Bid_amount > highest_bid:
            highest_bid = Bid_amount
            winner = bidder

    print(f"The winner is {winner}, with the highest bid of ${highest_bid}")

bids = {}

continue_bidding = True
while continue_bidding:

    user_name = input("Enter your name :" )
    bid_amount = int(input("Enter your bid amount :$ "))
    bids[user_name] = bid_amount
    should_continue = input("Are there any other bidders ? 'Yes' or 'No' : ").lower()
    if should_continue == "no":
      continue_bidding = False
      find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)



