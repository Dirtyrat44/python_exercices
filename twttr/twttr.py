def main():
    user_input = input("Input: ")
    print(vowel_eraser(user_input))

# Function to erase any vowels
def vowel_eraser(str):
    new_str = []
    for c in str:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            pass
        else:
            new_str.append(c)

    return "".join(new_str)




main()
