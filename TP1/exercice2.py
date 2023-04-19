import math
def resoudreEquation(a, b, c,):
    delta = (b**2)-(4*a*c)

    if delta < 0 :
        naPasDeSolution = True
        if naPasDeSolution:
            print('Aucune racine')
        return None

    if delta == 0 :
        aUneSeuleSolution = True
        if aUneSeuleSolution:

            print('Une seule racine')
            x1 = 0
        return x1

    if delta > 0 :
        aDeuxSolutions = True
        if aDeuxSolutions:
            print ('deux racines')
            x1 = ((-b - (delta**(1/2))) / (2 * a))
            x2 = ((-b + (delta**(1/2))) / (2 * a))
        return x1, x2

if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

print(resoudreEquation(a, b, c))