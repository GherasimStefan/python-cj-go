print("Curs 3")

x = 10
while x > 1:
    print("x este {}".format(x))
    x = x - 1
    continue

for i in range(1, 10, 2):
        print("i este {}".format(i))

for s in "some_string":
            print(s)


exemplu = "Acesta este un string"
print("prima litera din sir: {}".format(exemplu[0]))

l = len(exemplu)
print("lungimea sirului este de {}".format(l))

#print(exemplu[0])
#exemplu[4] = 'c'
#print(exemplu[0])

exemplu = "noua valoare"
print(exemplu)

exemplu2 = exemplu.replace('a', 'b')
print(exemplu)
print(exemplu2)

y = "100,123,2,5"
l = y.split(",")
print(l)

something = None
A = (1, 2, 1)
B = (1, 2, 1)
C = (2, 4, 7)

print(A)
print(B)
print(C)

print(A == B)
print(A ==C )

#A[1] = 8
#print(A[1])

inventar = ("faina", "drojdie", "apa", "sare")
print(inventar)

for item, value in enumerate(inventar):
    print("Produs {} => {}".format(item,value))

x = []
print(x)
if not x:
    print("Lista vida")
else:
    print("Lista are valori")

x = [True,
     False,
     "Ana",
     "are",
     "mere",
     2,
     3,
     ["un sir de caractere"],
     ("tuplu", 2)
 ]
print(x)
x[2] = "Ion"
print(x[2])
print(x)

inventar = ["faina", "drojdie", "apa", "sare"]
for item, value in enumerate(inventar):
    print("Produs {} => {}".format(item,value))

for element in inventar:
    print(element)

inventar.append("coca-cola")
print(inventar)
inventar += ["pepsi"]
print(inventar)

produse_noi = ["mere","pere","portocale"]

#inventar = inventar + produse_noi
print(inventar)
inventar.extend(produse_noi)
print(inventar)
# inventar.sor()
print(inventar)
print(sorted(inventar))
print(inventar)


inventar.reverse()
print(inventar)

print(inventar.count("mere"))
print(inventar.index("pere"))

inventar.insert(1,"avocado")
print(inventar)

l = inventar[:2] + ["banane"] + inventar[2:]
print(l)

lista = [
    0,
    1,
    [
        "al doilea nivel",
        ["al treilea nivel]", "abc"]
        ]
    ]
print(lista[2][0])

sir_nou = "acesta este un sir de caractere"
print(sir_nou[::])
print(sir_nou[::1])

s1 = set({1, 2, 3 ,4})
s2 = {3, 4, 5 , 6}
print(s1)
print(s2)

s1.add(9)
print(s1)
#l = (1, 2, 3, 4, 5, 6, 6, 9)
#print(l)
#s3 = set(l)
#l2 = list(s3)
#print(s3)
#print(12)

s1 = set({1, 2, 3, 4})
s2 = set({3, 4, 5, 6})

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)

print((s1 - s2) | (s2 - s1))

s2.add(9)
print(s2)
s2.discard(3)
print(s2)

d = {
    1:'a',
    2:'b'
}
print(d[2])

d2 = {
    '1': "Salut"
}

print(d2)

my_dict = {1: "home, 2: "office}

print(my_dict)
print(my_dict.get(3, 'Default'))
KEY = 3
if KEY in my_dict
    print("True")
else:
    print("False")