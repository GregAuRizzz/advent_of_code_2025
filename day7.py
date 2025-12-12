grille = []
try:
    while True:
        ligne = input()
        if ligne.strip() == "":
            continue
        grille.append(list(ligne))
except EOFError:
    pass

for j in range(len(grille[0])):
    if grille[0][j] == "S":
        start_col = j
        break

faisceaux = {(0, start_col)}
splits = 0

while faisceaux:
    nouveaux = set()
    for x, y in faisceaux:
        if x + 1 >= len(grille):
            continue
        case = grille[x + 1][y]
        if case == ".":
            nouveaux.add((x + 1, y))
        elif case == "^":
            if y - 1 >= 0:
                nouveaux.add((x + 1, y - 1))
            if y + 1 < len(grille[0]):
                nouveaux.add((x + 1, y + 1))
            splits += 1
    faisceaux = nouveaux

print(splits)
