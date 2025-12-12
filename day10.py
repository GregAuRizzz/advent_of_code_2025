import re
from collections import deque

total_appuis = 0

while True:
    try:
        ligne = input()
        if not ligne.strip():
            break

        match_cible = re.search(r'\[(.*?)\]', ligne) # Autre approche que pour les autres problèmes ;)
        texte_cible = match_cible.group(1)
        etat_cible = tuple(1 if c == '#' else 0 for c in texte_cible)
        
        nb_lumieres = len(etat_cible)
        etat_depart = tuple([0] * nb_lumieres)
        
        match_boutons = re.findall(r'\((.*?)\)', ligne)
        liste_boutons = []
        for m in match_boutons:
            indices = [int(x) for x in m.split(',')]
            liste_boutons.append(indices)
        
        file_attente = deque([(etat_depart, 0)])
        visites = set()
        visites.add(etat_depart)
        
        appuis_min = 0
        
        while file_attente:
            etat_actuel, distance = file_attente.popleft()
            
            if etat_actuel == etat_cible:
                appuis_min = distance
                break
            
            for bouton in liste_boutons:
                nouvel_etat_liste = list(etat_actuel)
                for index in bouton:
                    nouvel_etat_liste[index] = 1 - nouvel_etat_liste[index]
                
                nouvel_etat = tuple(nouvel_etat_liste)
                
                if nouvel_etat not in visites:
                    visites.add(nouvel_etat)
                    file_attente.append((nouvel_etat, distance + 1))
        
        total_appuis += appuis_min

    except EOFError:
        break

print(total_appuis)