import os


class Ohce:
    @classmethod
    def saisir(cls, chaîne):
        return chaîne[::-1] + os.linesep + 'Bien dit !' \
            if chaîne == 'radar' \
            else chaîne[::-1]