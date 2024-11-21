import os

from expressions import Expressions

class DetecteurPalindrome:
    @classmethod
    def saisir(cls, chaine):
        miroir = chaine[::-1]

        returned_value = Expressions.SALUTATION
        returned_value += miroir
        if miroir == chaine:
            returned_value += os.linesep + Expressions.FELICITATIONS
        returned_value += Expressions.ACQUITTANCE

        return returned_value