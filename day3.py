compteur = 0
try:
    while True:
        n = list(map(int, list(input().strip())))
        list_possible = []
        for i in range(len(n)):
            premier = n[i]
            deuxieme = -1
            for j in range(i+1, len(n)):
                if n[j] > deuxieme:
                    deuxieme = n[j]
            if deuxieme >= 0:
                list_possible.append(premier * 10 + deuxieme)
        compteur += max(list_possible)
except EOFError:
    pass
print(compteur)
