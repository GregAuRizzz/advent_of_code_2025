liste = []

try:
    while True:
        ligne = input().strip()
        if ligne == "":
            continue
        liste.append(list(ligne))
except EOFError:
    pass
delta = [(-1,-1), (-1,0), (-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
compteur_rouleaux = 0

for i in range(len(liste)):
    for j in range(len(liste[i])):
        if liste[i][j] != '@':
            continue
        compteur = 0
        for dx, dy in delta:
            x = i + dx
            y = j + dy
            if 0 <= x < len(liste) and 0 <= y < len(liste[x]):
                if liste[x][y] == '@':
                    compteur += 1
        if compteur < 4:
            compteur_rouleaux += 1

print(compteur_rouleaux)
