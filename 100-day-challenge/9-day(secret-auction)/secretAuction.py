print("Welcome to the SECRET AUCTION PROGRAM")

bid_data = []

def add_bid_data(name:str, bid_amount:float):
    bid_data.append({
        "name": name,
        "bid_amount": bid_amount
    })

do_you_want_to_bid = "yes"

while do_you_want_to_bid == "yes":
    name = input("What is your name? ")
    bid_amount = float(input("What's your bid? "))
    
    add_bid_data(name,bid_amount)

    do_you_want_to_bid = input("Are there any other bidders? Type 'yes' or 'no'.")

max_bid_index = 0

for i in range(len(bid_data)):
    if bid_data[i]["bid_amount"] > bid_data[max_bid_index]["bid_amount"]:
        max_bid_index = i


print(f"Winner of the bid is {bid_data[max_bid_index]['name']}, bid amount {bid_data[max_bid_index]['bid_amount']}")