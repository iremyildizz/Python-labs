from abc import abstractmethod, ABC
from typing import List, Tuple

from accessoire import Accessoire, TypeAccessoire
from elements_tiktok import ElementViral


# TODO Je suis abstraite et j'hérite de ElementViral
class Animal(ElementViral, ABC):
    @abstractmethod

    # Implantez mon constructeur
    def __init__(self, nom : str, nb_pattes : int) -> None:
        self.nom = nom
        self.nb_pattes = nb_pattes
        self.liste_accessoires = []


    def __add__(self, accessoire: Accessoire) -> int:
        # TODO Retournez le score viral de l'animal plus celui de l'accessoire
        return (self.score_viral() + accessoire.score_viral())

    def __iadd__(self, accessoire: Accessoire) -> 'Animal':
        # TODO Ajoutez l'accessoire à la liste de l'animal. Retournez l'animal en question
        #  Attention! Un animal n'ayant aucune patte ne peut enfiler des chaussures,
        if accessoire.type_accessoire == TypeAccessoire.CHAUSSURES and self.nb_pattes == 0:
            pass
        else:
            self.liste_accessoires.append(accessoire)
        return self
        
    @abstractmethod
    def crier(self) -> str:
        # TODO Rendez-moi abstraite
        pass

    def score_viral(self) -> int:
        # TODO Retournez la somme du score viral des accessoires présents dans la liste d'accessoires de l'animal
        score_tot = 0
        for accessoire in self.liste_accessoires:
           score_accessoire = Accessoire.score_viral(accessoire)
           score_tot += score_accessoire

        return score_tot


def calcul_meilleur_animal(animaux: List[Animal]) -> Tuple[str, int]:
    # TODO Retournez le nom et le score viral de l'animal ayant le score le plus haut
    minimum = 0
    nom = ""
    for animal in animaux:
        if animal.score_viral() > minimum :
            minimum = animal.score_viral()
            nom = animal.nom

    return nom, minimum
