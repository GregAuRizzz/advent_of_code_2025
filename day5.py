liste_range = [] 

try:
    while True:
        n = input()
        if n == "":
            break
        ligne_min, ligne_max = map(int, n.split("-"))
        liste_range.append((ligne_min, ligne_max))
except EOFError:
    pass
compteur = 0

try:
    while True:
        n = int(input())
        est_frais = False
        for rmin, rmax in liste_range:
            if rmin <= n <= rmax:
                est_frais = True
                break
        if est_frais:
            compteur += 1
except EOFError:
    pass

print(compteur)
