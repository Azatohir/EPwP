# Zadanie 1

def _filter(func=None, iterable=[]):

    if func is None:
        for x in iterable:
            if x:
                yield x
    else:
        for x in iterable:
            if func(x):
                yield x

    """Filtruje z iterable elementy, dla których funkcja func zwraca False zostawiając pozostałe"""


from types import GeneratorType

print(isinstance(_filter(), GeneratorType))
print(list(filter(lambda x: x > 0, [0, -3, 1, 6])) == list(_filter(lambda x: x > 0, [0, -3, 1, 6])))
print(list(filter(None, [2, -3, 1, 6])) == list(_filter(None, [2, -3, 1, 6])))
print(list(filter(None, [True, False, False])) == list(_filter(None, [True, False, False])))
print(list(filter(None, [0, -3, 1, 6])) == list(_filter(None, [0, -3, 1, 6])))

# Zadanie 2

def _map(func, iterable, *args):
    if args:
        for (x, y) in zip(iterable, *args):
            yield func(x, y)
    else:
        for x in iterable:
            yield func(x)
    """Mapuje elementy iterable na wartości fuknckji func"""


from types import GeneratorType
print(isinstance(_map(None, None), GeneratorType))
print(list(map(lambda x: x.upper(), 'ala ma kota')) == list(_map(lambda x: x.upper(), 'ala ma kota')))
print(list(map(lambda x,y: x+y, [1,2,3,4], [5,6,7,8])) == list(_map(lambda x,y: x+y, [1,2,3,4], [5,6,7,8])))

# Zadanie 3
def reverse_nonpalindromes(words):
    pal = lambda x: x == x[::-1]
    rev = lambda x: x[::-1]
    return list(map(rev, filter(lambda x: not pal(x), words)))

    """Zwraca listę odwróconych słowa które nie są palindromami.
    Palindromy zostają pominięte"""

print(reverse_nonpalindromes(["aa", "ab"])==["ba"])
print(reverse_nonpalindromes(["eht", "dog", "ala"])==["the", "god"])

# Zadanie 4
from functools import reduce

def squares_of_odds(values):
    oddN = filter(lambda x: x%2 != 0, values)
    squ = map(lambda x: x**2, oddN)
    return reduce(lambda a, b: a+b, squ)
    """Zwraca sumę kwadratów nieparzystych liczb"""

print(squares_of_odds([1,2,3,4,5,6])==35)
print(squares_of_odds([10, 13, 5, 6])==194)

#Zadanie 5
def all_are_positive(numbers):
    if not numbers:
        return True
    pos = lambda x: True if x > 0 else False
    tab = map(pos, numbers)
    return reduce(lambda a, b: False if a == False or b == False else True, tab)
    """zwraca czy wszystkie liczby są dodatnie"""
    #return all(n>0 for n in numbers)

print(all_are_positive([])) #PS: tu sie im wykraczy bez inicjalizatora :)
print(all_are_positive([1,2,3]))
print(not all_are_positive([-1,2,3]))
print(not all_are_positive([5,6,-2,1]))


#Zadanie 6
def flatten(lists): #lista list i ich sume, maja po 2 elementy
    return reduce(lambda a, b: a + list(filter(lambda x: x is not None, b)), lists)

print(flatten([[]])==[])
print(flatten([[1,2],[3,4]])==[1,2,3,4])
print(flatten([["1", 1.1],[]])==["1", 1.1])

#Zadanie 7

def celsius_to_fahrenheit(x):
    """Konwertuje liste temperatur w stopniach Celsjusza do skali Fahrenheita"""
    return map(lambda t: (9.0/5.0)*float(t) +32.0, x)

print(list(celsius_to_fahrenheit([0, 10, 100]))== [32.0, 50.0, 212.0])
print(list(celsius_to_fahrenheit([-123, 0])) == [-189.4, 32.0])

#Zadanie 8

from functools import reduce

def product_greater_than(x, k=0):
    """Zwraca iloczyn liczb w liście x większych od k"""
    return reduce(lambda a, b: a*b, filter(lambda w: w > k, x))

print(product_greater_than([1, 2, 3]) == 6)
print(product_greater_than([1, 2, 3], 2) == 3)
print(product_greater_than([-4, 5, 10, 23, 123], -5) == -565800)

#Zadanie 9
from functools import reduce

def create_sentence(x, k=0):
    """Łączy słowa (o długości co najmniej k) z listy x w zdanie - nie używa reduce"""
    return ' '.join(filter(lambda w: len(w) >= k, x))


print(create_sentence(['ala', 'ma', 'kota']) == 'ala ma kota')
print(create_sentence(['ala']) == 'ala')
print(create_sentence(['ala', 'ma', 'pieknego', 'kota'], k=3) == 'ala pieknego kota')

#Zadanie 10

def tuple_if_sum_greater(k, *lists):
    """Zwraca k-elementową krotke składającą się z kolejnych elementów list podanych jako arguemnty pozycyjne,
       jeżeli ich suma jest większa niż parametr k"""
    return list(map(lambda elements: tuple(elements), filter(lambda elements: sum(elements) > k, zip(*lists))))

print(list(tuple_if_sum_greater(0, [1,2,3])) == [(1,),(2,),(3,)])
print(list(tuple_if_sum_greater(4, [1,2,3], [2,3,4])) == [(2,3),(3,4)])
print(list(tuple_if_sum_greater(10, [1,2,3], [2,3,4])) == [])
print(list(tuple_if_sum_greater(0, [1,2], [3,4], [5,6])) == [(1,3,5), (2,4,6)])

#Zadanie 11
from math import sqrt

def primes(N):
    """Zwraca zbiór liczb pierwszych od 0 do N włącznie"""
    return set(filter(lambda p: all(p % w != 0 for w in range(2, p)), range(2, N+1)))

print(primes(5) == {2, 3, 5})
print(primes(10) == {2, 3, 5, 7})
print(primes(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                      43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})
