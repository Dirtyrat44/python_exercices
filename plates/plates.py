def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    new_s = []
    if len(s) >= 2 and len(s) <= 6:
        if s[0:2].isalpha():
            for c in s:
                if c.isdigit():
                    new_s.append(c)
                elif c.isalpha():
                    continue
                else:
                    return False
        else:
             return False
    else:
         return False
    for d in new_str if d.isdigit() and d[0] != 0 return True else: return False
         



# améliorations : Séparer la chaine au premier numéro rencontré pour vérifier si il ne commence pas par 0 et si il y a des numéros jusqu'à la fin
# valider aussi si la chaine n'a pas de numéro mais qu'elle >=2 ou <= 6
# chaine only isdigit() or isalpha()

main()

