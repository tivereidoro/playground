#!/usr/bin/python3
import os
# What is your name, how much are you bidding, Anyone else?

def check_highest(bidders_dict):
    """
    bidders_dict is a dictionary of bidders """
    highest_bid = 0
    for i in bidders_dict:
        if bidders_dict[i] > highest_bid:
            highest_bid = bidders_dict[i]
            highest_bidder = i
        else:
            continue
    return highest_bidder


print("\n****** Welcome to the Secret Auction ******\n")
bidders = {}
while True:
    name = input("What is your name.?: ")
    bid_amount = int(input("How much you bidding today?: "))
    bidders[name] = bid_amount

    done = input("\nAnyone else bidding.? (Enter y/n): ").lower()
    if done == 'y':
        os.system('clear')
        continue
    else:
        break

# sort for the highest
highest_bidder = check_highest(bidders)
print(bidders)
print(f"\n{highest_bidder} wins the auction with ${bidders[highest_bidder]}")
