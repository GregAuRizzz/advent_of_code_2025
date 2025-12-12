import math

liste = []
try:
    while(True):
        n = input().split()
        if n:
            try:
                liste.append([int(x) for x in n])
            except:
                liste.append(n)
except EOFError:
    pass

op = liste[-1]
n_lignes = len(liste) - 1
n_colonnes = len(op)
compteur = 0
for i in range(n_colonnes):
    current = [liste[ligne][i] for ligne in range(n_lignes)]

    if op[i] == "+":
        n = sum(current)
    elif op[i] == "*":
        n = math.prod(current)
    elif op[i] == "-":
        n = current[0]
        for x in current[1:]:
            n -= x
    elif op[i] == "/":
        n = current[0]
        for x in current[1:]:
            n /= x

    compteur += n
print(compteur)
