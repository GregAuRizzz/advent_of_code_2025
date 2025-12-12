import sys

def main():
    entree = sys.stdin.read().strip()
    segments = entree.split('\n\n')
    
    descriptions_formes = segments[:-1]
    commandes = segments[-1].strip().split('\n')
    
    surfaces_objets = {}
    
    for description in descriptions_formes:
        lignes = description.split('\n')
        identifiant = int(lignes[0].replace(':', ''))
        aire = 0
        for l in lignes[1:]:
            aire += l.count('#')
        surfaces_objets[identifiant] = aire
        
    nombre_valide = 0
    
    for ligne in commandes:
        partie_gauche, partie_droite = ligne.split(': ')
        l, h = map(int, partie_gauche.split('x'))
        quantites = map(int, partie_droite.split())
        
        surface_totale_disponible = l * h
        surface_requise = 0
        
        for idx, qte in enumerate(quantites):
            surface_requise += qte * surfaces_objets.get(idx, 0)
            
        if surface_requise <= surface_totale_disponible:
            nombre_valide += 1
            
    print(nombre_valide)

if __name__ == "__main__":
    main()