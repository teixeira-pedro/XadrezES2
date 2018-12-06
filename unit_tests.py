import unittest

import movimentos_pecas
# para executar os testes unitários, basta rodar no terminal 
# python -m unittest -v unit_tests.py

class TestStringMethods(unittest.TestCase):

    def test_is_preta(self):
        mock_tabuleiro=[
                            ['T','C','B','R','A','B','C','T'],
                            ['P','P','P','P','P','P','P','P'],
                            ['0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0'],
                            ['p','p','p','p','p','p','p','p'],
                            ['t','c','b','r','a','b','c','t'],
            ]
        self.assertEqual(movimentos_pecas.isPreta(mock_tabuleiro, 0, 0), 1)

if __name__ == '__main__':
    unittest.main()