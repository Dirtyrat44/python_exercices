def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    new_s = []
    if s[0:2].isalpha() and 6 < len(s) > 2:


    else:
        return False



# améliorations : Séparer la chaine au premier numéro rencontré pour vérifier si il ne commence pas par 0 et si il y a des numéros jusqu'à la fin
# valider aussi si la chaine n'a pas de numéro mais qu'elle >=2 ou <= 6
# chaine only isdigit() or isalpha()

main()


