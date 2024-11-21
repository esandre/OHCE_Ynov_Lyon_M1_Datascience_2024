import unittest

from ohce import Ohce


class MyTestCase(unittest.TestCase):
    def test_miroir(self):
        cas = ['test', 'ynov']

        for chaîne in cas:
            # ETANT DONNE une chaîne
            with self.subTest(chaîne):
                # QUAND on la saisit
                résultat = Ohce.saisir(chaîne)

                # ALORS elle est renvoyée en miroir
                self.assertEqual(chaîne[::-1], résultat)


if __name__ == '__main__':
    unittest.main()
