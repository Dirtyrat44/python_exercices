fruits_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "strawberries": 50,
    "plums": 70,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

def calories(t):
    if t in fruits_calories:
        return fruits_calories[t]
    else:
        return ""

def main():
    user_input = input("Item: ")
    print("Calories:", calories(user_input.lower()))





main()
