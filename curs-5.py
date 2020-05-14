print("curs 5 loaded")


class Coordinate(object):
    """ O coordonata e compusa din valorile x si y"""
    def __init__(self, x, y):
        """ Setam valorile pt x si y"""
        self.x = x
        self.y = y
    def __str__(self):
        """ Afisam coordonatele x si y"""
        return "<" +str(self.x) + "," + str(self.y) + ">"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        """ Returneaza distanta euclidiana dintre 2 coordonate"""
        x_diff_sq =(self.x - other.x) ** 2
        x_diff_sq =(self.y - other.y) ** 2

        return (x_diff_sq + y_diff_sq) ** 0.5


    def new(self):
        print("Something new")

origin = Coordinate(0,0)
c1 = Coordinate(1, 0)
c2 = Coordinate(1, 2)


print(c2)
print(origin)
origin.new()
c2.new()

print(c1 ==c1)



