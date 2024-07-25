def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))

# Function to erase any vowels
def shorten(str):
    return "".join([c for c in str if c.lower() not in ["a", "e", "i", "o", "u"]])



if __name__ == "__main__":
    main()
