import unittest

from ohce import Ohce


class MyTestCase(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND on la saisit
        résultat = Ohce.saisir(chaîne)

        # ALORS elle est renvoyée en miroir
        self.assertEqual('tset', résultat)

    def test_miroir_2(self):
        # ETANT DONNE une chaîne
        chaîne = 'ynov'

        # QUAND on la saisit
        résultat = Ohce.saisir(chaîne)

        # ALORS elle est renvoyée en miroir
        self.assertEqual('vony', résultat)


if __name__ == '__main__':
    unittest.main()
