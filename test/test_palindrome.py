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
                self.assertIn(chaîne[::-1], résultat)


    def test_felicitations(self):
        cas = ['radar', 'kayak']

        for palindrome in cas:
            with self.subTest(palindrome):
                # ETANT DONNE un palindrome

                # QUAND on le saisit
                résultat = Ohce.saisir(palindrome)

                # ALORS 'Bien dit !' est renvoyé après la chaîne
                self.assertEqual(palindrome + os.linesep + 'Bien dit !', résultat)

    def test_pas_bien_dit_sans_palindrom(self):
        # ETANT DONNE un non-palindrome
        non_palindrome = 'test'

        # QUAND on le saisit
        résultat = Ohce.saisir(non_palindrome)

        # ALORS 'Bien dit !' n'est pas renvoyé
        self.assertNotIn('Bien dit !', résultat)


if __name__ == '__main__':
    unittest.main()
