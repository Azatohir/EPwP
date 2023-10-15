# This is a sample Python script.

#laby 01
#Zadanie 1
def avg(input):
    return sum(input)/len(input)

print(avg([2,2,2,2,2,2]) - 2 < 0.0000001)
print(avg([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(avg([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)


def even_list(n):
    return [num for num in range(1, n+1) if num%2 == 0]

print(even_list(1) == [])
print(even_list(2) == [2])
print(even_list(-5) == [])
print(even_list(7) == [2,4,6])


def sum_of_squares(n):
    odp = 0
    for w in range(1, n+1):
        odp += pow(w, 2)
    return odp

print(sum_of_squares(1) == 1)
print(sum_of_squares(3) == 14)
print(sum_of_squares(10) == 385)


def sum_of_multiples(k, n=101):
    odp = 0
    for i in range(k, n, k):
        odp += i
    return odp

print(sum_of_multiples(5) == 1050)
print(sum_of_multiples(17) == 255)
print(sum_of_multiples(69) == 69)


from math import sqrt

def primes_less_than(N):
    return [num for num in range(2, N) if all(num%i !=0 for i in range(2, int(sqrt(num))+1))]


print(primes_less_than(5) == [2,3])
print(primes_less_than(10) == [2, 3, 5, 7])
print(primes_less_than(20) == [2, 3, 5, 7, 11, 13, 17, 19])


def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('ala') == True)
print(is_palindrome('ananas') == False)
print(is_palindrome('ananasa') == False)
print(is_palindrome('tomek') == False)


def how_many_different_letters(word):
    return len(set(list(word)))

print(how_many_different_letters('tomek') == 5)
print(how_many_different_letters('ala') == 2)
print(how_many_different_letters('ananas') == 3)
print(how_many_different_letters('jola') == 4)


def list_to_table(word):
    """ Funkcja przyjmuje 9-elementową liste i na jej podstawie tworzy stringa z HTMLową tabelą orzmiaru 3x3
    reprezentującą plansze do gry w kółko i krzyżyk"""
    board = '<table style="table-layout: fixed; height: 90px; width: 90px;">'

    for i in range(len(word)):
        if i%3 == 0:
            board += '\n'
        board += word[i]
        board += ' '

    board += "\n</table>"
    return board


print(list_to_table(['X', '', 'O', '', 'X', '', 'O', '', 'O']))


def zaprzyjaznione(n):
    w = []
    temp = []
    for i in range(2, n):
        if temp.count(i) == 0:
            sum1 = 1
            for j in range(2, i):
                if i%j == 0:
                    sum1 += j
            sum2 = 1
            for j in range(2,sum1):
                if sum1%j == 0:
                    sum2 += j
            if i == sum2 and sum1 != 1 and sum2 != 1 and sum1 != sum2:
                w.append((sum2, sum1))
                temp.append(sum1)
    return w


print(zaprzyjaznione(1) == [])
print(zaprzyjaznione(300) == [(220, 284)])
print(zaprzyjaznione(2000) == [(220, 284), (1184, 1210)])
print(zaprzyjaznione(13000) == [(220, 284), (1184, 1210),(2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595)])


def phi_euler(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
    if n > 1:
        result -= result // n

    return int(result)

print(phi_euler(6) == 2)
print(phi_euler(64) == 32)
print(phi_euler(97) == 96)

#Zadanie 2

def is_perfect(n):
    odp = 1
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            odp += i
    return odp == n


print(is_perfect(6) is True)
print(is_perfect(28) is True)
print(is_perfect(7) is False)


#Zadanie dodatkowe
def solve(d, m, tab):
    odp = 0
    for i in range(len(tab)-m+1):
        temp = 0
        for j in range(i, i+m):
            temp += tab[j]
        if temp == d:
            odp += 1
    return odp


tab=[1, 2, 1, 3, 2]
d=3
m=2
tab1=[1, 1, 1, 1, 1, 1]
d1=3
m1=2
tab2=[4,1,3,4,1,1,1,1,1,1,1]
d2=4
m2=4
print(solve(d, m, tab)==2)
print(solve(d1, m1, tab1)==0)
print(solve(d2, m2, tab2)==4)

#Zadanie dodatkowe 2
import re
def HowManyIntegers(n):
    odp = 0
    for num in range(1, n):
        num_str = str(num)
        if all(c in '0279' for c in num_str):
            odp += 1

    return odp

print(HowManyIntegers(1) == 0)
print(HowManyIntegers(10) == 3) # 2,7,9
print(HowManyIntegers(28) == 6) # 2,7,9,20,22,27

