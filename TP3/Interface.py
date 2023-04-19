# -*- coding: utf-8 -*-

import random

def saisirMatrice():
    #To do: Saisit une matrice d’adjacence au clavier
    nombreDeNoeuds = int(input("Donner le nombre de noeuds dans la matrice: "))
    nombreDePoids = int(input("Donner le nombre de poids dans la matrice: "))
    print("")
    matrice = []
    for i in range (nombreDeNoeuds):
        matrice.append([-1] * nombreDeNoeuds)
    for j in range (nombreDePoids):
        print("\t Saisir le poids " + str(j))
        dextrimite1 = int(input("\t\tDonner le noeud dextrémité 1: "))
        dextrimite2 = int(input("\t\tDonner le noeud dextrémité 2: "))
        poids = int(input("\t\tSaisir le poids: "))
        matrice[dextrimite1][dextrimite2] = poids
        matrice[dextrimite2][dextrimite1] = poids
    return matrice

def genereMatriceAleatoire(nb_noeuds):
    #Calcul pour trouver le nombre de connections necessaires pour s'approcher
    #a la moyenne cherchee en arrondisant vers l'entier grand.
    nb_noeuds = int(nb_noeuds)
    nb_poids = int(-(-(nb_noeuds / 2) ** 2) // 1)
    if nb_noeuds >= 0:
        matrice = []
        for i in range (nb_noeuds):
            matrice.append([-1] * nb_noeuds)
        compteur = 0
        while compteur < nb_poids:
            extrimite1 = random.randint(0,nb_noeuds-1)
            extrimite2 = random.randint(0,nb_noeuds-1)
            if extrimite1 != extrimite2 and matrice[extrimite1][extrimite2] == -1:
                compteur += 1
                poids = random.randint(1,99)
                matrice[extrimite1][extrimite2] = poids
                matrice[extrimite2][extrimite1] = poids
        return matrice
    else:
        print("le nombre de noeuds n'est pas un entier scalaire positif.")
        return "erreur"

def afficheChemin(predecesseurs, depart, arrive):
    #To do: Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs
        if depart >= 0 and arrive >= 0:
            noeud = arrive
            afficheur = f"{arrive}: FIN "    
            for i in range (len(predecesseurs)):
                if predecesseurs[i] >= -1:
                    while noeud != depart:
                        noeud = predecesseurs[noeud]
                        afficheur = f"{noeud}  ==> " + afficheur
                else:
                        print("un nombre de predecesseurs n'est pas un entier scalaire positif.")
                        return "erreur"
            afficheur = "DEBUT : " + afficheur
            chemin = f"Le chemin à parcourir est:\n\t{afficheur}\n"
            #print(chemin)
            return chemin
        else:
            print("Le départ ou l’arrivée n'est pas un entier positif scalaire.")
            return "error"
        

if __name__ == '__main__':
    # saisirMatrice()
    
    nb_noeuds = 5
    matAlea = genereMatriceAleatoire(nb_noeuds)
    txt = "la matrice aleatoire est: \n\t"
    for i in matAlea:
        for j in i:
            txt += "{}\t".format(j)
        txt += "\n\t"
    print(txt)
    
    predecesseurs = [-1, 0, 0, 2, 5, 2]
    depart = 0
    arrive = 4
    print(afficheChemin(predecesseurs, depart, arrive))
