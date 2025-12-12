import sys

graphe = {}

while True:
    try:
        ligne = input()
        if not ligne.strip():
            break
        parties = ligne.split(":")
        source = parties[0].strip()
        destinations = parties[1].strip().split()
        graphe[source] = destinations
    except EOFError:
        break
memoire = {}
def trouver_chemins(noeud):
    if noeud == 'out':
        return 1
    if noeud not in graphe:
        return 0
    if noeud in memoire:
        return memoire[noeud]
    total = 0
    for voisin in graphe[noeud]:
        total += trouver_chemins(voisin)
    memoire[noeud] = total
    return total
print(trouver_chemins('you'))