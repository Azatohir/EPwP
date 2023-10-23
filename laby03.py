# Laby 03

#Zadanie 1
#A
def log(* input):
    if input:
        message = ": ".join(map(str, input))
        print(message)

log("Hello World!") # Hello World!
log("The value is", 42) # The value is: 42

#B
def mean(* input):
    if input:
        w = sum(input)
        return w/len(input)
    return 0

print(mean(1,2,3) == 2)
print(mean(2,2,4,4) == 3)
print(mean(1,2,3,4,5,61,2,12,123,123) == 33.6)

#C
def check_dictionary_content(dic, **arg):
    for key, val in arg.items():
        if val > 0:
            if key in dic.keys():
                if dic[key] < val:
                    return False
            else:
                return False
    return True


d = {'orange': 3, 'apple': 1, 'dogs': 10}
print(check_dictionary_content(d, orange=2) == True)
print(check_dictionary_content(d, orange=2, apple=1) == True)
print(check_dictionary_content(d, dogs=11) == False)
print(check_dictionary_content(d, dogs=9, cats=0) == True)
print(check_dictionary_content(d, apple=0, cats=1) == False)
print(check_dictionary_content(d, **d) == True)

#Zadanie 2
def numbers_to_percents(values):
    if values:
        s = sum(values)
        odp = []
        for i in values:
            odp.append(i/s)
        return odp
    else:
        return []

print(numbers_to_percents([1,2,1])==[0.25, 0.5, 0.25])
print(numbers_to_percents([1])==[1])
print(numbers_to_percents([1,2,3,4])==[0.1, 0.2, 0.3, 0.4])

#Zadanie 3
def zwroc_rosnace(funkcja, *arg):
    return [odp for odp in arg if funkcja(odp) > odp]

def f1(n):
    return n**2-3*n

def f2(n):
    return 100-n

def f3(word):
    return word[::-1]

print(zwroc_rosnace(f1, 4, 6, 2, -5)==[6, -5])
print(zwroc_rosnace(f2, *range(100))==list(range(50)))
print(zwroc_rosnace(f3, "python", "nie", "jest", "bardzo", "fajny")==['jest', 'bardzo', 'fajny'])


#Zadanie 4
i = 0


def ile_wywolana():
    global i
    i = i+1
    return i

print(ile_wywolana()==1)
print(ile_wywolana()==2)
print(ile_wywolana()==3)


#Zadanie 5
from math import sqrt


def get_primes(number):
    num = number
    while True:
        bylo = False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i != 0:
                bylo = True
                break
        if not bylo and num > 1:
            yield num
        num = num + 1

#Zadanie 6


#A
def natural_numbers(k=0):
    i = k
    while True:
        yield k
        k += 1


import types

print(isinstance(natural_numbers(), types.GeneratorType))

for i, n in enumerate(natural_numbers()):
    print(i, i == n)
    if i > 20:
        break

for i, n in enumerate(natural_numbers(1)):
    print(i, i + 1 == n)
    if i > 20:
        break


#B
def factorials():
    num = 2
    i = 2
    yield 1
    yield 1
    while True:
        yield num
        i += 1
        num = num*i

import types
print(isinstance(factorials(), types.GeneratorType))

results = [1, 1, 2, 6, 24, 120, 720, 5040]
for truth, answer in zip(results, factorials()):
    print(truth, truth == answer)

#Zadaie 7


def Fibonaccie():
    num1 = 0
    num2 = 1
    yield 0
    yield 1
    while True:
        num1, num2 = num2, num1 + num2
        yield num2


#test
import types
print(isinstance(Fibonaccie(), types.GeneratorType))

results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for truth, answer in zip(results, Fibonaccie()):
    print(truth, truth == answer)
