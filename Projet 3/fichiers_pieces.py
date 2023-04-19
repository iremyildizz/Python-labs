import pandas as pd

from constantes import CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS, FICHIER_CAPSULE, FICHIERS_RESERVOIRS, \
    FICHIERS_MOTEURS

def ppl2Dictionnaire(file: str) -> dict: 
    valeurs = {}
    with open(file, mode ='r') as ppl_file: 
        for line in ppl_file.readlines():
            if line[0] == "#" or line[0] == "\n" or len(line) == 0:
                pass
            else:
                ihatedatabases = line.find('=')
                key = line[:ihatedatabases]
                value = line[ihatedatabases + 1:].strip("\n")
                if key != "nom":
                    if key == "impulsion specifique":
                        value = int(value)
                    else:
                        value = float(value)
                valeurs[key] = (value)
    return valeurs


def charger_capsules_df(chemin_capsules: str) -> pd.DataFrame:
    # TODO Retournez un dataframe des capsules décrites dans le fichier FICHIER_CAPSULE
    #  Il faut aussi renommer les colonnes pour que celles-ci soient plus lisibles
    df =(pd.read_csv(chemin_capsules + "/" + FICHIER_CAPSULE))
    df.columns = ['nom', 'hauteur', 'masse', 'prix', 'places']
    return df
    


def charger_reservoirs_df(chemin_reservoirs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des réservoirs décrits dans
    #  les fichiers FICHIERS_RESERVOIRS
    df = pd.DataFrame()
    for jsonfile in FICHIERS_RESERVOIRS:
        file = chemin_reservoirs + '/' + jsonfile
        df = df.append(pd.DataFrame(pd.read_json(file)), ignore_index=True)
    return df


def charger_moteurs_df(chemin_moteurs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des moteurs décrits dans
    #  les fichiers FICHIERS_MOTEURS
    dfList = []
    for files in FICHIERS_MOTEURS:
        file = chemin_moteurs + "/" + files
        dfList.append(ppl2Dictionnaire(file))
    df = pd.DataFrame(dfList)
    return df


def filtrer_moteurs(moteurs_df: pd.DataFrame, impulsion_minimum: int) -> pd.DataFrame:
    # TODO Retourner un sous-ensemble filtré d'un df de moteurs
    #  où l'impulsion spécifique est au dessus d'un certain seuil
    newdf = pd.DataFrame(moteurs_df[moteurs_df['impulsion specifique'] > impulsion_minimum])
    return newdf


if __name__ == '__main__':
    # charger_capsules_df
    capsules = charger_capsules_df(CHEMIN_CAPSULES)
    print(capsules)
    print()

    #charger_reservoirs_df
    reservoirs = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    print(reservoirs)
    print()

    # charger_moteurs_df
    moteurs = charger_moteurs_df(CHEMIN_MOTEURS)
    print(moteurs)
    print()

    # filtrer_moteurs
    moteurs_filtres = filtrer_moteurs(moteurs, 220)
    print(moteurs_filtres)
    
    