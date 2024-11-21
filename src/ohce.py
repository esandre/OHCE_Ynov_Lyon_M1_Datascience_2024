import os


class Ohce:
    @classmethod
    def saisir(cls, chaîne):
        miroir = chaîne[::-1]

        return ('Bonjour' + os.linesep + miroir + os.linesep
                + 'Bien dit !' + os.linesep + 'Au revoir') \
            if chaîne == miroir \
            else ('Bonjour' + os.linesep + miroir
                  + os.linesep + 'Au revoir')