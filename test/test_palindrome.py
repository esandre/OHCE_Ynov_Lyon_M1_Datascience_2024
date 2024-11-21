import os
import random
import string
import unittest

from ohce import Ohce


class MyTestCase(unittest.TestCase):
    @staticmethod
    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_miroir(self):
        cas = ['test', 'ynov', self.randomword(10)]

        for chaîne in cas:
            # ETANT DONNE une chaîne
            with self.subTest(chaîne):
                # QUAND on la saisit
                résultat = Ohce.saisir(chaîne)

                # ALORS elle est renvoyée en miroir
                self.assertEqual(chaîne[::-1], résultat)


    def test_felicitations(self):
        # ETANT DONNE un palindrome
        palindrome = 'radar'

        # QUAND on le saisit
        résultat = Ohce.saisir(palindrome)

        # ALORS 'Bien dit !' est renvoyé après la chaîne
        self.assertEqual(palindrome + os.linesep + 'Bien dit !', résultat)

if __name__ == '__main__':
    unittest.main()
