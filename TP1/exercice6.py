import matplotlib.pyplot as plt
import math
import numpy as np
2
def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe, a=None):
    a = nombreComplexe.real
    b = nombreComplexe.imag
    module = math.sqrt(a**2 + b**2)
    return module

def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)
    print(round(module, 3), round(angle, 3))

    a = nombreComplexe.real
    b = nombreComplexe.imag

    resultat = complex(math.cos(angle_rotation * math.pi/180), math.sin(angle_rotation* math.pi/180) * nombreComplexe)
    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)
    print(round(nouveauModule, 3), round(nouvelAngle, 3))
    return resultat


def dessiner(number, label):
    if number != None:
        plt.polar([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
