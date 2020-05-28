from functools import reduce
print("Curs-7")
#lambda
a = [(1, 8), (3, 1), (5, 6), (7, 9)]
a.sort(key=lambda x: x[1])

print(a)

#filter
number_list = range(-5, 5)
print(list(number_list))
less_than_zero = list(filter(lambda x: x <= 0, number_list))

print(less_than_zero)

#MAP
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

print(squared)

squared = list(map(lambda x: x**2, items))
print(squared)


#REDUCE

product = 1
l = [1, 2, 3, 4]
for num in l:
    product = product *num

print(product)


product = reduce(lambda x, y: x*y, l)

print(product)

#1. se da o lista de elemente intregi; sa se calculeze suma elementelor - folosind lambda

inputList = [1, 4, 6, 13, 5]
listSum = reduce(lambda a, b: a+b, inputList)
print(inputList)

#2

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
result_dict = {
    k.lower(): mcase.get(k.lower(), 0) +mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(result_dict)