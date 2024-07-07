def main():
    amount = 50

    while amount != 0:
        while True:
            amount_due(amount)
            user_input = input("Insert Coin: ")
            if user_input == 25:
                return amount - 25
            elif user_input == 10:
                return amount - 10
            elif user_input == 5:
                return amount - 5
            else:
                True
            if amount == 0:
                break






def amount_due(n):
    print(f"Amount Due: {n}")









main()
