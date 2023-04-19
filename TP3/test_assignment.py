# -*- coding: utf-8 -*-

import unittest
import os
import sys
import pickle
import tarfile
from unittest.mock import patch
import copy


from Algo import indiceMinimum, noeudMinimalNonVisitesDeNoeud, noeudMinimalNonVisites, noeudsVoisins, dijkstra
from Interface import saisirMatrice, genereMatriceAleatoire, afficheChemin


algo_data = 'Expected/Algo.spydata'
interface_data = 'Expected/Interface.spydata'

algo_tar = tarfile.open(algo_data, "r")
interface_tar = tarfile.open(interface_data, "r")

algo_tar.extractall()
interface_tar.extractall()

extracted_files = algo_tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
        with open(f, 'rb') as fdesc:
            algo_data_ex = pickle.loads(fdesc.read())

extracted_files = interface_tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
        with open(f, 'rb') as fdesc:
            interface_data_ex = pickle.loads(fdesc.read())
            
            
class TestAlgo(unittest.TestCase):

    def testIndiceMinimum(self):
        vec     = copy.deepcopy(algo_data_ex['vec'])
        tuple_1 = indiceMinimum(vec)
        tuple_2 = algo_data_ex['res_1']
        self.assertTupleEqual(tuple_1, tuple_2)
    
    def testNoeudMinimalNonVisitesDeNoeudA(self):
        matrice = copy.deepcopy(algo_data_ex['matrice'])
        noeud   = algo_data_ex['noeud_1']
        noeudsVisites = copy.deepcopy(algo_data_ex['noeuds_vis_1'])
        tuple_1 = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeudsVisites)
        tuple_2 = algo_data_ex['res_2']
        self.assertTupleEqual(tuple_1, tuple_2)
       
    def testNoeudMinimalNonVisitesDeNoeudB(self):
        matrice = copy.deepcopy(algo_data_ex['matrice'])
        noeud   = algo_data_ex['noeud_1']
        noeudsVisites = copy.deepcopy(algo_data_ex['noeuds_vis_2'])
        tuple_1 = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeudsVisites)
        tuple_2 = algo_data_ex['res_3']
        self.assertTupleEqual(tuple_1, tuple_2)
       
    def testnoeudMinimalNonVisites(self):
        matrice = copy.deepcopy(algo_data_ex['matrice'])
        noeudsVisites = algo_data_ex['noeuds_vis_3']
        tuple_1 = noeudMinimalNonVisites(matrice, noeudsVisites)
        tuple_2 = algo_data_ex['res_4']
        self.assertTupleEqual(tuple_1, tuple_2)
        
           
    def testNoeudsVoisinsA(self):
        matrice = copy.deepcopy(algo_data_ex['matrice'])
        noeud   = algo_data_ex['noeud_1']
        tuple_1 = noeudsVoisins(matrice, noeud)
        tuple_2 = algo_data_ex['res_5']
        self.assertTupleEqual(tuple_1, tuple_2)  
                                   
    def testNoeudsVoisinsB(self):
        matrice = copy.deepcopy(algo_data_ex['matrice'])
        noeud   = algo_data_ex["noeud_2"]
        tuple_1 = noeudsVoisins(matrice, noeud)
        tuple_2 = algo_data_ex['res_6']
        self.assertTupleEqual(tuple_1, tuple_2)
        
    def testDijkstra(self):
        matrice = copy.deepcopy(algo_data_ex['matrice'])
        depart  = algo_data_ex["depart"]
        arrive  = algo_data_ex["arrive"]
        tuple_1 = dijkstra(matrice, depart, arrive)
        tuple_2 = algo_data_ex['res_7']
        self.assertTupleEqual(tuple_1, tuple_2)

class TestInterface(unittest.TestCase):

    @patch('builtins.input', side_effect=[3, 2, 0, 1, 10, 2, 1, 5])
    def testSaisirMatrice(self, mock_inputs):
        matrice = [[-1, 10, -1], [10, -1, 5], [-1, 5, -1]]
        self.assertListEqual(saisirMatrice(), matrice)
    
    def testGenereMatriceAleatoireA(self):
        self.assertTrue(isinstance(genereMatriceAleatoire(5), list))
        
    def testGenereMatriceAleatoireB(self):
        nb_noeud = 5
        matrice = genereMatriceAleatoire(nb_noeud)
        result = True
        for i, ligne in enumerate(matrice):
            if len(ligne) != nb_noeud:
                result = False         
            for j, elem in enumerate(ligne):
                if (i == j) and elem != -1:
                    result = False
                elif elem < -1 or elem == 0 or elem > 100 or matrice[i][j] != matrice[j][i]:
                    result = False            
        self.assertTrue(result)
    
    def testAfficheChemin(self):
        predecesseurs = copy.deepcopy(interface_data_ex["predecesseurs"])
        depart = interface_data_ex["depart"]
        arrive = interface_data_ex["arrive"]
        txt = afficheChemin(predecesseurs, depart, arrive)
        self.assertMultiLineEqual(interface_data_ex["txt"], txt)
        
    
if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
