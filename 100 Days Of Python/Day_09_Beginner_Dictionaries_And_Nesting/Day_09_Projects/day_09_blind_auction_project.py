logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


def highest_bidder(bidder_dic):
    '''This Function tells who is the highest bidder.!'''
    highest_bid = 0
    winner = ""
    for bid in bidder_dic:
        if bidder_dic[bid] > highest_bid:
            highest_bid = bidder_dic[bid]
            winner = bid

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")


bid_dict = {}

bid_over = False

while not bid_over:
    user = input("Enter your name: ").capitalize()
    price = int(input("Enter your price: $"))
    bid_dict[user] = price
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if continue_bid == "no":
        bid_over = True
        highest_bidder(bid_dict)
    else:
        print("\n" * 20)   
