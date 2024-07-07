def main():
    amount = 50

    while amount > 0:
        amount_due(amount)
        user_input = int(input("Insert Coin: "))
        if user_input in [25, 10, 5]:
            amount -= user_input


    print(f"Change Owed: {amount * -1}")



def amount_due(n):
    print(f"Amount Due: {n}")









main()
