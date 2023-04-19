from abc import abstractmethod, ABC
from typing import List

from animal import Animal


# TODO Je suis abstraite et j'hérite de Animal
class Oiseau (Animal, ABC):
    @abstractmethod
    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self,nom, nb_pattes, chante = bool) -> None:
        super().__init__(nom, nb_pattes)
        self.chante = chante

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_OISEAU NOM_OISEAU ne chante pas.
        #  ou
        #  Le TYPE_OISEAU NOM_OISEAU chante.

        if self.chante == True:
            return f"Le {type(self).__name__} {self.nom} chante."
        else:
            return f"Le {type(self).__name__} {self.nom} ne chante pas."
        
    def crier(self) -> str:
        # TODO Je dois retourner "cuicui" si je ne chante pas.
        #  Sinon, retournez les deux premières phrases du refrain de September:
        #  Ba de ya, say that you remember. Ba de ya, dancing in September.
        if self.chante == False:
            return "cuicui"
        else:
            return "Ba de ya, say that you remember. Ba de ya, dancing in September."
        


# TODO J'hérite de Oiseau
class Cockatiel(Oiseau): 
    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom, nb_pattes) -> None:
        super().__init__(nom, nb_pattes, chante = True)
        
