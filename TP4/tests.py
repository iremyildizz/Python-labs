import unittest
from unittest import TestCase
from fonctions_a_tester import fizz_buzz, resoudre_equation

class TestFizzBuzz(TestCase):

    def test_fizz_buzz_3(self):
        nombre = 27
        result = "fizz"
        self.assertEqual(fizz_buzz(nombre),result)

    def test_fizz_buzz_5(self):
        nombre = 20
        result = "buzz"
        self.assertEqual(fizz_buzz(nombre), result)

    def test_fizz_buzz_3_5(self):
        nombre = 30
        result = "fizzbuzz"
        self.assertEqual(fizz_buzz(nombre), result)


    def test_fizz_buzz_non_facteur(self):
        nombre = 43
        result = str(nombre)
        self.assertEqual(fizz_buzz(nombre), result)
        #  et assurez-vous que la valeur en sotie soit une string

class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        self.assertEqual(resoudre_equation(1, 1, 2), None)
        #  et assurez-vous que la valeur en sortie est None

    def test_resoudre_equation_une_racine(self):
        self.assertEqual(resoudre_equation(1, 0, 0), 0)

    def test_resoudre_equation_deux_racine(self):
        result = -1, -4
        self.assertEqual(resoudre_equation(1, 5, 4), result)


if __name__ == '__main__':
    unittest.main()
