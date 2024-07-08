def main():
    user_input = input("Input: ")
    print(vowels_eraser(user_input))

# Function to erase any vowels
def vowels_eraser(str):
    new_str = []
    for c in str:
        if c.lower() in ["a", "e", "i", "o", "u"]:




main()
