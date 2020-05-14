print("Curs 4")
#nr = input("Va rugam introduceti un nr")
#try:
 #   nr = int(nr) * 2
  #  print("Dublul numarului este: {}".format(nr))
#except:
 #   print("A aparut o eroare")
#else:
 #   print("Totul e ok! {}")

# Functions

#def my_func():
 #   print("My very first function")

  #  return

#result = my_func()
#print("Result is {}".format(result))

#def A():
#    print("Ex 1")
#def B():
#    print("Ex 2")

#def C():
#    A()
#    B()

#C()


#def adunare(param1, param2):
#    """
#    prints the sum of the two params
#    :param param1:
#    :param param2:
#    :return: none
#    """
#    suma = param1 + param2
#    return suma

#primul_nr = input("Introdu primul numar: \n")
#al_doilea_nr = input("Introdu al doilea numar: \n")
#print(adunare(int(primul_nr), int(al_doilea_nr)))

#def ziNastere(nume, prenume, varsta=18):
#    print("Buna {}! La multi ani pt cei {} ani!".format(nume, prenume, varsta))

#ziNastere(varsta=20, nume="Ionut", prenume="Popa")
#ziNastere(nume="Cristian", varsta=30, prenume="Popa")
#ziNastere(nume="Maria", prenume="Popa")

#global x
#x = 2

#def Test():
#    x = 3
#    print(x)


#print(x)
#Test()
#print("Daca apelam functia Test(), vom avea rezultatul")

#def Suma(a, b, *c):
#    """ adunam cel putin 2 parametrii"""
#    x = a + b
#    if c:
#        print("c => {}".format(c))
#        for e in c:
#            x = x + e
#
#    return x
#
#print(Suma(1,2))
#print(Suma(1, 2, 3, 4, 5))

def F(b, **a):
    print(a)
    print(b)

F("Parametrul b", unu= 1, doi= 2)

Adunare = lambda a, b: a + b
print(Adunare(1, 2))

Cub = lambda x: x**3

print(Cub(2))

