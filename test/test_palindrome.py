import unittest

class MyTestCase(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE une chaîne
        chaîne = 'test'

        # QUAND on la saisit
        résultat = Ohce.saisir(chaîne)

        # ALORS elle est renvoyée en miroir
        self.assertEqual('tset', résultat)


if __name__ == '__main__':
    unittest.main()
