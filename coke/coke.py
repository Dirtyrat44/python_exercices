def main():
    amount = 50
    
    while amount_due != 0:
        amount_due(amount)
        user_input = input("Insert Coin: ")
        while True:
            if user_input == 25:
                return amount - 25
            elif user_input == 10:
                return amount - 10
            elif user_input == 5:
                return amount - 5
            else:
                return True






def amount_due(n):
    print(f"Amount Due: {n}")









main()
