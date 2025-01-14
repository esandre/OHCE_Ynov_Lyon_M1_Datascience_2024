import os
import random
import string
import unittest
from itertools import chain

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
                self.assertIn(palindrome + os.linesep + 'Bien dit !', résultat)

    def test_pas_bien_dit_sans_palindrom(self):
        # ETANT DONNE un non-palindrome
        non_palindrome = 'test'

        # QUAND on le saisit
        résultat = Ohce.saisir(non_palindrome)

        # ALORS 'Bien dit !' n'est pas renvoyé
        self.assertNotIn('Bien dit !', résultat)

    def test_bonjour(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND on la saisit
        résultat = Ohce.saisir(chaîne)

        # ALORS 'Bonjour' est renvoyé avant elle
        attendu = 'Bonjour' + os.linesep
        self.assertEqual(attendu, résultat[:len(attendu)])

    def test_au_revoir(self):
        cas = ['test', 'radar']

        for chaîne in cas:
            with self.subTest(chaîne):
                # ETANT DONNE une chaîne

                # QUAND on la saisit
                résultat = Ohce.saisir(chaîne)

                # ALORS 'Au revoir' est renvoyé en dernier
                attendu = os.linesep + 'Au revoir'
                self.assertEqual(attendu, résultat[-len(attendu):])


if __name__ == '__main__':
    unittest.main()
