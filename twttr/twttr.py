def main():
    user_input = input("Input: ")
    print("Output:", vowel_eraser(user_input))

# Function to erase any vowels
def vowel_eraser(str):
    return "".join([c for c in str if c.lower() not in ["a", "e", "i", "o", "u"]])




main()
