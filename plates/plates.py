def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    new_s = []
    new_s_digit = []
    # Check if first 2 are alpha, if min len is 2 and max len is 6 and if s doesn't contain ponctuation
    if s[0:2].isalpha() and 6 >= len(s) > 1 and all (c not in [" ", "'", "."] for c in s):
        for c in s:
            if c.isdigit():
                new_s.append(c)
        if new_s[0:1] == "0" and is not new_s.isdigit():
            return False





# améliorations : Séparer la chaine au premier numéro rencontré pour vérifier si il ne commence pas par 0 et si il y a des numéros jusqu'à la fin
# valider aussi si la chaine n'a pas de numéro mais qu'elle >=2 ou <= 6
# chaine only isdigit() or isalpha()

main()


