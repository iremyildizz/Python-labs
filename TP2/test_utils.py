"""
utils.py
Fichier contenant des fonctions utilitaires pour l'exécution des tests.
                  NE PAS TOUCHER !!!!!!!!!!!!!!

"""

import _thread
import threading
import unittest


# Timeout
def exitFunction():
    _thread.interrupt_main()


def timeout(s):
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, exitFunction)
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result

        return inner

    return outer


# Test basique
class TestBasique(unittest.TestCase):

    @timeout(2)  # Termine le programme quand l'execution dure plus d'une seconde
    def executer_test(self, fonction, nom_fonction_testee):
        self.executer_test_sans_timeout(fonction, nom_fonction_testee)

    def executer_test_sans_timeout(self, fonction, nom_fonction_testee):
        try:
            fonction()
        except KeyboardInterrupt:
            self.fail(
                f'L\'appel fonction {nom_fonction_testee} ne se termine pas --> Verifiez vos boucles')
        except AssertionError as e:
            raise e
        except:
            self.fail(
                f'Une exception a ete levee lors de l\'appel fonction {nom_fonction_testee}. Reverifier votre code')
