# -*- coding: utf-8 -*-

from Interface import saisirMatrice, genereMatriceAleatoire, afficheChemin
from Algo import dijkstra


def meilleurCheminDijkstra():
    print('Quel activité voulez-vous faire?\n','1- Saisir une matrice personnalisé.')
    print(' 2- Générer aléatoirement une matrice.\n','3- Charger une carte topographique')

    choix = int(input('>'))
  
    if (choix == 1):
        matrice = saisirMatrice()
    elif (choix == 2):
        nbSommets = input('Donner le nombre de sommets : ')
        matrice = genereMatriceAleatoire(nbSommets)
    else:
        print('Choix invalide.')
        return
    
    depart = int(input('Donner le noeuds de depart : '))
    arrive = int(input('Donner le noeuds d''arrivée : '))

    [distance, predecesseurs]  = dijkstra(matrice, depart, arrive)
    print('La distance minimale est ', distance)
    afficheChemin(predecesseurs, depart, arrive)
    

if __name__ == '__main__':
    meilleurCheminDijkstra()

