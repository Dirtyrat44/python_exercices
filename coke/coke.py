def main():
    amount = 50

    while amount != 0:
        while True:
            amount_due(amount)
            user_input = int(input("Insert Coin: "))
            if user_input == 25:
                amount -= 25
            elif user_input == 10:
                amount -= 10
            elif user_input == 5:
                amount -= 5
            else:
                True







def amount_due(n):
    print(f"Amount Due: {n}")









main()
