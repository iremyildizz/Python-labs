from typing import List

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from constantes import DELTA_V_MINIMUM_PAR_CORPS_CELESTE, CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS
from fichiers_pieces import charger_capsules_df, charger_moteurs_df, charger_reservoirs_df
from fusee import Fusee, Capsule, Reservoir, Moteur


def creer_capsules(capsules_df: pd.DataFrame) -> List[Capsule]:
    # TODO Transformez le dataframe des capsules en liste d'objets de type Capsule
    listeCapsule = []
    capsulesDf2Array = np.array(capsules_df)
    for i in range (len(capsulesDf2Array)):
        nom = capsulesDf2Array[i][0]
        hauteur = capsulesDf2Array[i][1]
        masse = capsulesDf2Array[i][2]
        prix = capsulesDf2Array[i][3]
        places = capsulesDf2Array[i][4]
        listeCapsule.append(Capsule(nom, hauteur, masse, prix, places))
        
    return listeCapsule


def creer_moteurs(moteurs_df: pd.DataFrame) -> List[Moteur]:
    # TODO Transformez le dataframe des moteurs en liste d'objets de type Moteur
    listeMoteur = []
    Df2Array = np.array(moteurs_df)
    for i in range (len(Df2Array)):
        nom = Df2Array[i][0]
        hauteur = Df2Array[i][1]
        masse = Df2Array[i][2]
        prix = Df2Array[i][3]
        imp_spe = Df2Array[i][4]
        listeMoteur.append(Moteur(nom, hauteur, masse, prix, imp_spe))
    return listeMoteur


def creer_reservoirs(reservoirs_df: pd.DataFrame) -> List[Reservoir]:
    # TODO Transformez le dataframe des reservoir en liste d'objets de type Reservoir
    listeReservoir = []
    Df2Array = np.array(reservoirs_df)
    for i in range (len(Df2Array)):
        nom = Df2Array[i][0]
        hauteur = Df2Array[i][1]
        masse = Df2Array[i][2]
        prix = Df2Array[i][3]
        capacité = Df2Array[i][4]
        listeReservoir.append(Reservoir(nom, hauteur, masse, prix, capacité))
    return listeReservoir
    pass


def corps_celestes_accessibles(fusee: Fusee) -> List[str]:
    # TODO Retournez la liste des corps célestes accessibles par la fusée.
    #  Utiliser DELTA_V_MINIMUM_PAR_CORPS_CELESTE
    deltaV = fusee.calculer_deltav()
    listeee = list(DELTA_V_MINIMUM_PAR_CORPS_CELESTE.keys())
    corpsCelesteAccessibles = []
    deltaVValues = list(DELTA_V_MINIMUM_PAR_CORPS_CELESTE.values())
    for i in range (len(deltaVValues)):
        if deltaVValues[i] < deltaV:
            corpsCelesteAccessibles.append(listeee[i])

    return corpsCelesteAccessibles


def comparer_fusee(fusee_1: Fusee, fusee_2: Fusee) -> None:
    # TODO créer un grouped barplot comparant les fusées passées en paramètre en fonction des trois métriques suivantes:
    #  * Masse / Coût
    #  * DeltaV / Coût
    #  * DeltaV / Masse
    # TODO Générez un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio
    deltaVmasse1 = fusee_1.calculer_deltav() / fusee_1.masse
    deltaVmasse2 = fusee_2.calculer_deltav() / fusee_2.masse
    deltaVprix1 = fusee_1.calculer_deltav() / fusee_1.prix
    deltaVprix2 = fusee_2.calculer_deltav() / fusee_2.prix
    hauteurmasse1 = fusee_1.hauteur / fusee_1.masse
    hauteurmasse2 = fusee_2.hauteur / fusee_2.masse

    # Génère un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio
    d = {'fusée': [fusee_1.nom, fusee_1.nom, fusee_1.nom,
            fusee_2.nom, fusee_2.nom, fusee_2.nom], 
        'Ratios': [deltaVmasse1, deltaVprix1, hauteurmasse1, 
            deltaVmasse2, deltaVprix2, hauteurmasse2], 
        'type_ratio': ['deltaV/masse', 'deltaV/prix', 'hauteur/masse', 
            'deltaV/masse', 'deltaV/prix', 'hauteur/masse']}
    df = pd.DataFrame(d)
    sns.catplot(data=df, x='fusée', y='Ratios', hue='type_ratio', kind='bar')
    plt.show(block=True)



if __name__ == '__main__':
    # creer_capsules
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    capsules = creer_capsules(capsules_df)
    for capsule in capsules:
        print(capsule)
    print()

    # creer_moteurs
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)
    moteurs = creer_moteurs(moteurs_df)
    for moteur in moteurs:
        print(moteur)
    print()

    # creer_reservoirs
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    reservoirs = creer_reservoirs(reservoirs_df)
    for reservoir in reservoirs:
        print(reservoir)
    print()

    # corps_celestes_accessibles
    capsule = Capsule("PasDBonSens", 1.5, 840.0, 600.0, 1)
    reservoir_1 = Reservoir("Piscine", 25.0, 9000.0, 13000.00, 6480.0)
    moteur = Moteur("La Puissance", 12.0, 15000.0, 39000.00, 295)
    fusee_1 = Fusee("Romano Fafard", capsule, reservoir_1, moteur)
    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")

    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")
    print()

    # comparer_fusee
    reservoir_2 = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    fusee_2 = Fusee("Romano Fafard Lite", capsule, reservoir_2, moteur)
    comparer_fusee(fusee_1, fusee_2)
