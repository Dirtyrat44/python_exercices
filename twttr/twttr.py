def main():
    user_input = input("Input: ")
    print(vowel_eraser(user_input))

# Function to erase any vowels
def vowel_eraser(str):
    return "".join([c for c in str.lower() not in []"a", "e", "i", "o", "u"])




main()
