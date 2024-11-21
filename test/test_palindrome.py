import os
import random
import string
import unittest

from detecteur_palindrome import DetecteurPalindrome
from expressions import Expressions


class PalindromeTest(unittest.TestCase):
    @staticmethod
    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    CAS_PALINDROME = ['radar', 'kayak']
    CAS_NON_PALINDROME = ['test', 'chat', 'ynov']

    def test_miroir(self):
        cas = self.CAS_NON_PALINDROME + [self.randomword(10)]

        for chaine in cas:
            # ETANT DONNE une chaîne
            with self.subTest(chaine):
                # QUAND je la saisis
                resultat = DetecteurPalindrome.saisir(chaine)

                # ALORS elle est renvoyée en miroir
                miroir = chaine[::-1]
                self.assertIn(miroir, resultat)

    def test_bonjour(self):
        cas = [self.CAS_NON_PALINDROME[0], self.CAS_PALINDROME[0]]

        for chaine in cas:
            # ETANT DONNE une chaîne
            with self.subTest(chaine):
                # QUAND je la saisis
                resultat = DetecteurPalindrome.saisir(chaine)

                # ALORS "Bonjour" est envoyé avant la réponse
                self.assertEqual(Expressions.SALUTATION,
                                 resultat[:len(Expressions.SALUTATION)])

    def test_au_revoir(self):
        cas = [self.CAS_NON_PALINDROME[0], self.CAS_PALINDROME[0]]

        for chaine in cas:
            # ETANT DONNE une chaîne
            with self.subTest(chaine):
                # QUAND je la saisis
                resultat = DetecteurPalindrome.saisir(chaine)

                # ALORS "Au revoir" est envoyé après la réponse
                self.assertEqual(Expressions.ACQUITTANCE,
                                 resultat[-len(Expressions.ACQUITTANCE):])

    def test_palindrome_felicitations(self):
        cas = self.CAS_PALINDROME

        for palindrome in cas:
            # ETANT DONNE un palindrome
            with self.subTest(palindrome):
                # QUAND je le saisis
                resultat = DetecteurPalindrome.saisir(palindrome)

                # ALORS "Bien dit !" suit immédiatement le mot
                self.assertIn(palindrome + os.linesep + Expressions.FELICITATIONS,
                              resultat)


if __name__ == '__main__':
    unittest.main()

# TODO : Gérer les sauts de ligne
# TODO : Gérer les espaces