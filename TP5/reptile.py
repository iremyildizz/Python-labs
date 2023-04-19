from abc import abstractmethod, ABC
from typing import List

from animal import Animal


# TODO Je suis abstraite et j'hérite de Animal
class Reptile(Animal, ABC):
    @abstractmethod
    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom, nb_pattes, est_nocturne = bool):
        super().__init__(nom, nb_pattes)
        self.est_nocturne = est_nocturne

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_REPTILE NOM_REPTILE est nocturne.
        #  ou
        #  Le TYPE_REPTILE NOM_REPTILE est diurne.
        if self.est_nocturne: 
            return f"Le {type(self).__name__} {self.nom} est nocturne."
        else:
            return f"Le {type(self).__name__} {self.nom} est diurne."


# TODO J'hérite de Reptile
class Serpent(Reptile):

    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom, est_nocturne, est_venimeux = bool):
        super().__init__(nom, 0, est_nocturne)
        self.est_venimeux = est_venimeux

    def __str__(self) -> str:
        # TODO Ajouter les phrases suivantes à la chaine de base de Reptile:
        #  Il est venimeux.
        #  ou
        #  Il n'est pas venimeux.
        #  Utilisez la methode __str__ de Reptile avec: super(Serpent, self).__str__()
        if self.est_venimeux == False:
            return f"{super(Serpent, self).__str__()} Il n'est pas venimeux."
        if self.est_venimeux == True:
            return f"{super(Serpent, self).__str__()} Il est venimeux."


    def crier(self) -> str:
        # TODO Retournez le cri du serpent: sssss
        return "sssss"
