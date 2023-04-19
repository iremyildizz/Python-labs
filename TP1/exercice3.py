
SECONDESENANNEES = 31536000
SEMAINESTOTALES = 52.143
JOURSTOTALS = 7
HEURESTOTALES = 24
MINUTESTOTALES = 60
SECONDESTOTALES = 60

def resteDe(nombre):
    return nombre - int(nombre)

def decomposer(sec):
    annees = sec / SECONDESENANNEES
   
    semaines = resteDe(annees) * SEMAINESTOTALES

    jours = resteDe(semaines) * JOURSTOTALS

    heures = resteDe(jours) * HEURESTOTALES

    minutes = resteDe(heures) * MINUTESTOTALES

    secondes = resteDe(minutes) * SECONDESTOTALES
    
    return(str(int(annees)) + " annees, " + 
           str(int(semaines)) + " semaines, " + 
           str(int(jours)) + " jours, " + 
           str(int(heures)) + " heures, " + 
           str(int(minutes)) + " minutes, " + 
           str(int(secondes)) + " secondes")

while True :
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))


