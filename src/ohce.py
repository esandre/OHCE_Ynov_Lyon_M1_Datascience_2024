import os


class Ohce:
    @classmethod
    def saisir(cls, chaîne):
        miroir = chaîne[::-1]

        return miroir + os.linesep + 'Bien dit !' \
            if chaîne == miroir \
            else miroir