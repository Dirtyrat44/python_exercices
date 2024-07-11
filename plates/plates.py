

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Vérifiez si les deux premiers sont alphabétiques, si la longueur est entre 2 et 6 et s'il n'y a pas de ponctuation
    if s[0:2].isalpha() and 2 <= len(s) <= 6 and all(c not in [" ", "'", "."] for c in s):
        digit_seen = False
        for i, c in enumerate(s):
            if c.isdigit():
                digit_seen = True
                # Si le premier chiffre est '0' ou s'il y a des non-chiffres après un chiffre
                if c == '0' or not s[i:].isdigit():
                    return False
                break
        if not digit_seen:  # Si aucun chiffre n'est trouvé, cela reste valide tant que c'est alphabétique
            return True
        return digit_seen  # Retourne True si un chiffre a été vu et toutes les vérifications sont passées
    else:
        return False

main()
