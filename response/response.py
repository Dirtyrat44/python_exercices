import validators


def main():
    print(email_check(input("What's your email adress? ")))


def email_check(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
