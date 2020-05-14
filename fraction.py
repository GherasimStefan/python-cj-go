"""
    Scrieti o clasa Fraction(numarator si numitor)
    care sa implementeze urmatoarele metode:
           - __init__ : instantiem numarator si numitor
           - __str__  : afisam "numarator/numitor
           - __add__  : returnam o noua fractie care reprezinta adunarea
           - __sub__  : returnam o noua fractie care reprezinta scaderea
           - inverse: : returneaza inversa fractiei

"""

class Fration(object):
    """
    implementare fractie
    """
    def __init__(self, numarator, numitor):
        assert type(numarator) == int and type(numitor) == int, "folositi int, va rog"
        self.numarator = numarator
        self.numitor = numitor

a = Fration(1, 2)
b = Fration(1, 2)

print(a == b)


