from abc import abstractmethod, ABC
from enum import Enum
from typing import List

from animal import Animal


class LongueurPoils(Enum):
    RASES = 0
    COURTS = 1
    LONGS = 2

    def __str__(self):
        return self.name


# TODO Je suis abstraite et j'hérite de Animal
class Mammifere(Animal, ABC):
    @abstractmethod
    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom, nb_pattes, longueur_poils) -> None:
        super().__init__(nom, nb_pattes)
        self.longueur_poils = longueur_poils
    

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_MAMMIFERE NOM_MAMMIFERE a NB_PATTES pattes et des poils LONGUEUR_POILS.
        return f"Le {type(self).__name__} {self.nom} a {self.nb_pattes} pattes et des poils {self.longueur_poils}."
        


# TODO J'hérite de Mammifere
class Chat(Mammifere):

    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom, longueur_poils, couleur) -> None:
        super().__init__(nom, 4, longueur_poils)
        self.couleur = couleur

    def crier(self) -> str:
        # TODO Retournez le cri du chat: Miaou
        return "Miaou"
