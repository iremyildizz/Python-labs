"""
Fichier contenant les tests.
                  NE PAS TOUCHER !!!!!!!!!!!!!!

"""
import exercice1 as ex1
import exercice2 as ex2
import exercice3 as ex3
import exercice4 as ex4

import unittest
import os
import sys

from test_utils import TestBasique

class TestExercice1(TestBasique):
    dic_1 = {'a': 5, 'b': 2, 'c': 9}
    dic_1_copy = dic_1.copy()
    dic_2 = {'a': 1, 'b': 8, 'd': 17}
    dic_2_copy = dic_2.copy()
    result = {'a': 5, 'b': 8, 'd': 17, 'c': 9}

    def test1_combine_dic1(self):
        def fonction():
            dic_3 = ex1.combine_dic(self.dic_1, self.dic_2)
            self.assertDictEqual(dic_3, self.result)
        self.executer_test(fonction, 'test1_combine_dic1')

    def test1_combine_dic2(self):
        def fonction():
            dic = {}
            dic_3 = ex1.combine_dic(self.dic_1, dic)
            self.assertEqual(dic_3, self.dic_1_copy)
        self.executer_test(fonction, 'test1_combine_dic2')


class TestExercice2(TestBasique):
    def test2_tri_bulle1(self):
        def fonction():
            val = [5, 8, 1, 9, 6, 2, 4, 3, 7, 5]
            result = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
            sorted_val = ex2.tri_bulle(val)
            self.assertEqual(result, sorted_val)
        self.executer_test(fonction, 'test2_tri_bulle1')


    def test2_tri_bulle2(self):
        def fonction():
            val = []
            result = []
            sorted_val = ex2.tri_bulle(val)
            self.assertEqual(result, sorted_val)

        self.executer_test(fonction, 'test2_tri_bulle2')

    def test2_tri_bulle3(self):
        def fonction():
            val = [5, 2, 4, 8, 6, 1, 5, 75, 12, 72, 4, 8, 1, 0, 45, 1, 4584, 1, 4, 4, 1, 4, 8, 10]
            result = [0, 1, 1, 1, 1, 1, 2, 4, 4, 4, 4, 4, 5, 5, 6, 8, 8, 8, 10, 12, 45, 72, 75, 4584]
            sorted_val = ex2.tri_bulle(val)
            self.assertEqual(result, sorted_val)

        self.executer_test(fonction, 'test2_tri_bulle3')


class TestExercice3(TestBasique):
    pi = 3.141592653589793

    def test3_compute_pi1(self):
        def fonction():
            p = 5
            computed_pi, nb_iter = ex3.compute_pi(p)
            result_nb_iter = 200001
            result_pi = round(self.pi, p)
            result_pi = int(result_pi * 10 ** p)
            computed_pi = int(computed_pi * 10 ** p)
            self.assertEqual(result_nb_iter, nb_iter)
            self.assertEqual(result_pi, computed_pi)

        self.executer_test(fonction, 'test3_compute_pi1')

    def test3_compute_pi2(self):
        def fonction():
            p = 4
            computed_pi, nb_iter = ex3.compute_pi(p)
            result_nb_iter = 20001
            result_pi = round(self.pi, p)
            result_pi = int(result_pi * 10 ** p)
            computed_pi = int(computed_pi * 10 ** p)
            self.assertEqual(result_nb_iter, nb_iter)
            self.assertEqual(result_pi, computed_pi)

        self.executer_test(fonction, 'test3_compute_pi2')


class TestExercice4(TestBasique):
    player_pos = [0, 0]
    maze = [['O', 'W', '_', '_', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', '_', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
    def test41_init_maze1(self):
        def fonction():
            nb_row = 4
            nb_col = 7
            player_pos = [0, 0]
            end_pos = [3, 6]
            walls = [(0, 1), (1, 1), (1, 2), (1, 3), (1, 5), (2, 1), (2, 5), (3, 3), (3, 5)]
            maze = ex4.init_maze(nb_row, nb_col, player_pos, end_pos, walls)
            self.assertEqual(maze, self.maze)

        self.executer_test(fonction, 'test41_init_maze1')

    def test41_init_maze2(self):
        def fonction():
            nb_row = 10
            nb_col = 6
            player_pos = [0, 2]
            end_pos = [9, 2]
            walls = [(0, 1), (1, 1), (1, 2), (1, 3), (1, 5), (2, 1), (2, 5), (3, 3), (3, 5), (8, 2), (8, 3), (7, 5), (6,5)]
            maze = ex4.init_maze(nb_row, nb_col, player_pos, end_pos, walls)
            result = [['_', 'W', 'O', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W'], ['_', 'W', '_', '_', '_', 'W'], ['_', '_', '_', 'W', '_', 'W'], ['_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', 'W'], ['_', '_', '_', '_', '_', 'W'], ['_', '_', 'W', 'W', '_', '_'], ['_', '_', 'X', '_', '_', '_']]
            self.assertEqual(maze, result)

        self.executer_test(fonction, 'test41_init_maze2')

    def test42_validate_move1(self):
        def fonction():
            result = ex4.validate_move(self.maze, [1, 0])
            self.assertTrue(result)

        self.executer_test(fonction, 'test42_validate_move1')

    def test42_validate_move2(self):
        def fonction():
            result = ex4.validate_move(self.maze, [-1, 0])
            self.assertFalse(result)

        self.executer_test(fonction, 'test42_validate_move2')

    def test42_validate_move3(self):
        def fonction():
            result = ex4.validate_move(self.maze, [0, -1])
            self.assertFalse(result)

        self.executer_test(fonction, 'test42_validate_move3')

    def test42_validate_move4(self):
        def fonction():
            result = ex4.validate_move(self.maze, [4, 0])
            self.assertFalse(result)

        self.executer_test(fonction, 'test42_validate_move4')

    def test42_validate_move5(self):
        def fonction():
            result = ex4.validate_move(self.maze, [0, 7])
            self.assertFalse(result)

        self.executer_test(fonction, 'test42_validate_move5')

    def test42_validate_move6(self):
        def fonction():
            result = ex4.validate_move(self.maze, [0, 1])
            self.assertFalse(result)

        self.executer_test(fonction, 'test42_validate_move6')

    def test43_move1(self):
        def fonction():
            maze = self.maze.copy()
            player_pos = self.player_pos.copy()
            maze, player_pos = ex4.move('j', maze, player_pos)
            self.assertEqual(maze, self.maze)
            self.assertEqual(player_pos, self.player_pos)

        self.executer_test(fonction, 'test43_move1')

    def test43_move2(self):
        def fonction():
            maze = self.maze.copy()
            player_pos = self.player_pos.copy()
            maze, player_pos = ex4.move('s', maze, player_pos)
            result_maze = [['_', 'W', '_', '_', '_', '_', '_'], ['O', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', '_', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            result_player_pos = [1, 0]
            self.assertEqual(maze, result_maze)
            self.assertEqual(player_pos, result_player_pos)

        self.executer_test(fonction, 'test43_move2')

    def test43_move3(self):
        def fonction():
            maze = [['_', 'W', '_', '_', '_', '_', '_'], ['O', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', '_', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            player_pos = [1, 0]
            maze, player_pos = ex4.move('w', maze, player_pos)
            result_maze = [['O', 'W', '_', '_', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', '_', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            result_player_pos = [0, 0]
            self.assertEqual(maze, result_maze)
            self.assertEqual(player_pos, result_player_pos)

        self.executer_test(fonction, 'test43_move3')

    def test43_move4(self):
        def fonction():
            maze = self.maze.copy()
            player_pos = self.player_pos.copy()
            maze, player_pos = ex4.move('a', maze, player_pos)
            self.assertEqual(maze, self.maze)
            self.assertEqual(player_pos, self.player_pos)

        self.executer_test(fonction, 'test43_move4')

    def test43_move5(self):
        def fonction():
            maze = self.maze.copy()
            player_pos = self.player_pos.copy()
            maze, player_pos = ex4.move('w', maze, player_pos)
            self.assertEqual(maze, self.maze)
            self.assertEqual(player_pos, self.player_pos)

        self.executer_test(fonction, 'test43_move5')

    def test43_move6(self):
        def fonction():
            maze = self.maze.copy()
            player_pos = self.player_pos.copy()
            maze, player_pos = ex4.move('d', maze, player_pos)
            self.assertEqual(maze, self.maze)
            self.assertEqual(player_pos, self.player_pos)

        self.executer_test(fonction, 'test43_move6')

    def test43_move7(self):
        def fonction():
            maze = [['_', 'W', '_', '_', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', 'O', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            player_pos = [2, 3]
            maze, player_pos = ex4.move('d', maze, player_pos)
            result_maze = [['_', 'W', '_', '_', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', '_', 'O', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            result_player_pos = [2, 4]
            self.assertEqual(maze, result_maze)
            self.assertEqual(player_pos, result_player_pos)

        self.executer_test(fonction, 'test43_move7')

    def test43_move8(self):
        def fonction():
            maze = [['_', 'W', '_', '_', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', '_', 'O', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            player_pos = [2, 3]
            maze, player_pos = ex4.move('a', maze, player_pos)
            result_maze = [['_', 'W', '_', '_', '_', '_', '_'], ['_', 'W', 'W', 'W', '_', 'W', '_'], ['_', 'W', 'O', '_', '_', 'W', '_'], ['_', '_', '_', 'W', '_', 'W', 'X']]
            result_player_pos = [2, 2]
            self.assertEqual(maze, result_maze)
            self.assertEqual(player_pos, result_player_pos)

        self.executer_test(fonction, 'test43_move8')


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
