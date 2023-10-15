# This is a sample Python script.

#Zadanie 1
def check_anagram(first, second):
    if len(first) != len(second):
        return False
    return sorted(first) == sorted(second)

print(check_anagram("abcd", "dcba") == True)
print(check_anagram("aba", "baa") == True)
print(check_anagram("aba", "ba") == False)
print(check_anagram("tom marvolo riddle ", "i am lord voldemort") == True)

#Zadanie 2
def gaderypoluki(text, key):
    keys = key.lower()
    nKey = list(keys)
    text = text.lower()
    s = ''
    for i in range(0, len(text)):
        if text[i] == ' ':
            s += ' '
        ind = keys.find(text[i])
        if ind != -1:
            if ind%2 == 0:
                s += key[ind+1]
            else:
                s += key[ind-1]
        else:
            if text[i] != ' ':
                s += text[i]

    return s.lower()

print(gaderypoluki('Ala ma kota', 'GADERYPOLUKI') == 'gug mg iptg')
print(gaderypoluki('gug mg iptg', 'GADERYPOLUKI') == 'ala ma kota')

#Zadanie 3

#Funkcja 1
def even_numbers_from_list(data):
    return [num for num in data if num%2 == 0]

print(even_numbers_from_list([1, 2, 3, 4]) == [2, 4])
print(even_numbers_from_list(range(10)) == list(range(0, 10, 2)))
print(even_numbers_from_list(range(1000)) == list(range(0, 1000, 2)))
print(even_numbers_from_list([10, 2, 3, 4, 6, -3, -4]) == [10, 2, 4, 6, -4])

#Funkcja 2
def words_analyze(words):
    return [(words.index(wor), wor, len(wor)) for wor in words]


print(words_analyze(['tomek', 'jadzia']) == [(0, 'tomek', 5), (1, 'jadzia', 6)])
print(words_analyze([]) == [])

#Funkcja 3
def count_words_starting_with_given_letter(text, letter):
    return {word: text.split().count(word) for word in set(text.split()) if word.startswith(letter)}

print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'o') == {'ola': 2, 'o': 1})
print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'k') == {'kota': 1})
print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'x') == {})

#Zadanie 4
def merge_dicts(a, b, f):
    odp = {}

    for key, value in a.items():
        odp[key] = value

    for key, value in b.items():
        if key in odp:
            odp[key] = f(odp[key], value) # nowa wartosc za pomoca funkcji f!! a nie zwykly +!!
        else:
            odp[key] = value

    return odp

def add(a,b):
    return a + b

print(merge_dicts({'a': 1}, {'b': 1}, add) == {'b': 1, 'a': 1})
print(merge_dicts({'a': 1, 'b': 2}, {'b': 1}, add) == {'b': 3, 'a': 1})
print(merge_dicts({'a': 1, 'b': 2}, {'b': 1, 'c': 3, 'a': 7}, add) == {'c': 3, 'b': 3, 'a': 8})

#Zadanie 5
from math import sqrt


def primes(N):
    return {num for num in range(2, N+1) if all(num%i != 0 for i in range(2, int(sqrt(num))+1))}


print(primes(5) == {2, 3, 5})
print(primes(10) == {2, 3, 5, 7})
print(primes(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})

#Zadanie 6
def func1(n):
    return [(i, f) for i in range(0, n) for f in range(0, n) if i < n and f < n]

print(func1(3)==[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
print(func1(0)==[])

def func2(n):
    return [(i, f) for i in range(0, n) for f in range(0, n) if i < f]

print(func2(3)==[(0, 1), (0, 2), (1, 2)])
print(func2(4)==[(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])

def func3(n):
    return [(i, f) for i in range(0, n) for f in range(0, n) if i > f]

print(func3(3)==[(1, 0), (2, 0), (2, 1)])
print(func3(4)==[(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)])

#Zadanie 7
from itertools import combinations
def powerset(x):
    l = list(x)
    odp = []
    for i in range(len(l)+1):
        for subset in combinations(l, i):
            odp.append(list(subset))

    w = odp[3]
    odp[3] = odp[4]
    odp[4] = w
    return odp


print(powerset('abc')==[[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']])
print(powerset([1, 2, 3])==[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
print(powerset(['abc', 5, 6])==[[], ['abc'], [5], ['abc', 5], [6], ['abc', 6], [5, 6], ['abc', 5, 6]])

#Zadanie 8
def primes(N):
    return {num for num in range(2, N+1) if all(num%i !=0 for i in range(2, int(sqrt(num))+1))}
from math import sqrt


def help_primes(N, i):
    if i == 1:
        return True
    if N % i != 0:
        return help_primes(N, i-1)
    else:
        return False


def primes_extra_b(N, i=2):
    if i > N:
        return set()

    if i == 2:
        return {2} | primes_extra_b(N, i+1)

    if help_primes(i, int(sqrt(i)+1)):
        return {i} | primes_extra_b(N, i+1)
    else:
        return primes_extra_b(N, i+1)


print(primes_extra_b(5) == {2, 3, 5})
print(primes_extra_b(10) == {2, 3, 5, 7})
print(
    primes_extra_b(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                            53, 59, 61, 67, 71, 73, 79, 83, 89, 97})