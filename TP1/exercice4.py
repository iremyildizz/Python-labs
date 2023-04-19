import math

def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):

    acceleration = ((vitesseFinale-vitesseInitiale)*0.2778)/duree

    positionFinale = (vitesseInitiale*0.2778)*duree + ((0.5)*acceleration*(duree**2)) + positionInitiale
    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
