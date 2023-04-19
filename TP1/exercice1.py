def fizzBuzz(n):
    if n % 5 == 0 and n % 3 == 0 :
        print("fizzbuzz")

    elif n % 5 == 0 :
        print("buzz")

    elif n % 3 == 0 :
        print("fizz")

    else :
        print("nothing")

    #  Assigner ensuite la valeur à la variable resultat et retourner celle-ci avec le mot-clé return.


#resultat = n
#return resultat

number = int(input("indiquez le nombre: "))
fizzBuzz(number)
