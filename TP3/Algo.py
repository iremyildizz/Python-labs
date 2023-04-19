# -*- coding: utf-8 -*-

def indiceMinimum(vec): 
    #To do: Trouve l’indice et la valeur minimum dans un vecteur
    minimum = vec[0]
    indice = 0   
    for i in range(len(vec)):
        if (type(vec[i]) == int or type(vec[i]) == float) and vec[i]>= -1 :
            if minimum == -1 or (vec[i] != -1 and vec[i] < minimum):
                minimum = vec[i]
                indice = i
        else:
            print("N'est pas plus grand que -1 ou n'est pas un numero")
            return "error", "error"
    return indice, minimum

    
def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    #To do: Cherche le nœud non visité ayant le poids minimum autour d’un nœud spécifique
    if noeud >= 0:
        for j in range (len(noeuds_vis)):
            if noeuds_vis[j] >= 0:
                liste = matrice[noeud]
                if len(matrice) == len(liste) and noeud in noeuds_vis:
                    for i in range(len(liste)):
                        if (type(liste[i]) == int or type(liste[i]) == float) and liste[i]>= -1 :
                            for n in noeuds_vis:
                                if i == n:
                                    liste[i] = -1
                        else:
                            print("N'est pas plus grand que -1 ou n'est pas un numero")
                            return"erreur", "erreur"
                else:
                    print("N'est pas une carée ou le noeud n'est pas dans la liste de noeud visité")
                    return "erreur", "erreur"
            else:
                print("Le nœud visité n'est pas un entier positif scalaire")
                return "erreur", "erreur"
    else:
        print("Le nœud n'est pas un entier positif scalaire")
        return "erreur", "erreur"
    indice, minimum = indiceMinimum(liste)
    return indice, minimum

def noeudMinimalNonVisites(matrice,noeuds_vis):
    if len(matrice) == len(matrice[0]):
        depart = 0
        arrive, minimum = noeudMinimalNonVisitesDeNoeud(matrice, depart, noeuds_vis)
        for n in range(len(noeuds_vis)):
            if noeuds_vis[n] >= 0:
                for i in range (len(matrice)):
                    for j in range(len(matrice)):
                        if matrice[i][j] >= -1:
                                if j in noeuds_vis:
                                    arrive2, minimum2 = noeudMinimalNonVisitesDeNoeud(matrice, j, noeuds_vis)
                                    if minimum2 < minimum:
                                        arrive = arrive2
                                        depart = j
                        else:
                            print("N'est pas plus grand que -1")
                            return "error", "error"
            else:
                print("Le nœud visité n'est pas un entier positif scalaire")
                return "error", "error"
    else:
        print("N'est pas une carée")
        return "error", "error"
    return depart, arrive
    #To do: Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins
    #To do: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)


def noeudsVoisins(matrice, noeud):
    #To do: Cherche les nœuds voisins et leur poids par rapport à un nœud initial.
    lesPoids = []
    lesNoeuds = []
    if len(matrice) == len(matrice[noeud]):
        for n in range(len(matrice)):
            if matrice[n][noeud] >= -1:
                if matrice[n][noeud] != -1:
                    lesPoids.append(matrice[n][noeud])
                    lesNoeuds.append(n)
            else:
                print("N'est pas plus grand que -1")
                return "error", "error"
    else:
        print("La matrice n'est pas une carée")
        return "error", "error"
    return lesNoeuds, lesPoids

def dijkstra(matrice, depart, arrive):
    noeudVisites = []
    distanceMin = []
    predecesseurs = []
    if len(matrice) == len(matrice[depart]):
        if depart >= 0 and arrive >= 0:
                for i in range (len(matrice)):
                    distanceMin.append(-1)
                    predecesseurs.append(-1)
                distanceMin[depart] = 0
                noeudCourant = depart
                noeudVisites.append(noeudCourant)
                if noeudCourant >= -1:
                        while len(noeudVisites) != len(matrice) and noeudCourant != arrive:
                            lesNoeuds, lesPoids = noeudsVoisins(matrice, noeudCourant)
                            for j in range (len(lesNoeuds)):
                                distance = distanceMin[noeudCourant] + lesPoids[j]
                                if distance < distanceMin[lesNoeuds[j]] or distanceMin[lesNoeuds[j]] == -1:
                                    distanceMin[lesNoeuds[j]] = distance
                                    predecesseurs[lesNoeuds[j]] = noeudCourant
                            noeudCourant = noeudMinimalNonVisites(matrice,noeudVisites)[1]
                            noeudVisites.append(noeudCourant)
                        distance = distanceMin[arrive]
                else:
                    print("N'est pas plus grand que -1")
                    return "error", "error"
        else:
            print("La matrice n'est pas une carée")
            return "error", "error"
    else:
        print("Le départ ou l’arrivée n'est pas un entier positif scalaire.")
        return "error", "error"
    return distance, predecesseurs


if __name__ == '__main__':
    vec     = [-1, 4, 6, -1, -1, 3, 5]
    indice, minimum = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1, 2, 3]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 1
    noeudsVoisins(matrice, noeud)
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 3
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    depart  = 0
    arrive  = 3
    indice, prédécesseurs = dijkstra(matrice, depart, arrive)
    txt = "la distance la plus courte entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
    print(txt.format(depart, arrive, indice, prédécesseurs))
        