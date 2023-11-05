#laby 06
import re
#Zadanie 2
pattern = r'RUN\s\d{6}\sCOMPLETED\.\sOUTPUT\sIN\sFILE\s.*\.dat\.$'

file_path = 'atoms (1).txt'
with open(file_path) as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            print(line)


#Zadanie 3
pattern = r'Invalid user (\w*) from ([\d.]+)'

file_path = 'messages(1).txt'
with open(file_path) as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            print(line)

#Zadanie 4
from collections import defaultdict

def count_letters(word):
    my_dict = defaultdict(int)
    for letter in set(word):
        my_dict[letter] = len(re.findall(letter, word))
    return my_dict
    """ Zwraca slownik gdzie kluczami sa litery, a wartosci ilosc ich wystepowania """



print(count_letters('aaaaa') == {'a': 5})
print(count_letters('abbccaaaa') == {'a': 5, 'b': 2, 'c': 2})
print(count_letters('abc') == {'a': 1, 'b': 1, 'c': 1})

def group_words_by_first_letter(text):
    my_dict = defaultdict(int)
    for word in text.split(' '):
        i = word[0]
        pattern = r'\b'+re.escape(i)+r'\w+'
        my_dict[i] = re.findall(pattern, text)
    print(dict(my_dict))
    return dict(my_dict)

    """ Dzieli tekst po spacjach i zwraca slownik gdzie kluczami sa pierwsze litery, a wartosciami listy slow zaczynajacych sie na te litery"""


print(group_words_by_first_letter("ala ma kota") == {'a': ['ala'], 'm': ['ma'], 'k': ['kota']})
print(group_words_by_first_letter("ala ma kota ala ma psa") == {'a': ['ala', 'ala'], 'm': ['ma', 'ma'], 'k': ['kota'], 'p': ['psa']})
print(group_words_by_first_letter("ala ma kota ale marysia ma konia") == {'a': ['ala', 'ale'], 'm': ['ma', 'marysia', 'ma'], 'k': ['kota', 'konia']})

#Zadanie 5
class FrozenDictionary(object):
    """
    Odpowiednik frozenset dla zbiorów, czyli słownik, który nie jest modyfikowalny,
    a dzięki temu może być np. elementem zbiorów, albo kluczem w innym słowniku.
    """

    def __init__(self, dictionary):
        """Tworzy nowy zamrożony słownik z podanego słownika"""
        self._frozen_dict = dictionary
        self._has_val = hash(frozenset(dictionary.items()))

    def __hash__(self):
        """Zwraca hasz słownika (int)"""
        return self._has_val

    def __eq__(self, d):
        """Porównuje nasz słownik z zamrożonym słownikiem d"""
        if isinstance(d, FrozenDictionary):
            return d._frozen_dict == self._frozen_dict
        return False

    def __repr__(self):
        """Zwraca reprezentację naszego słownika jako string"""
        return repr(self._frozen_dict)


dicts = [FrozenDictionary({'ala': 4}),
         FrozenDictionary({'ala': 1, 'jacek': 0}),
         FrozenDictionary({'ala': 4}),
         FrozenDictionary({'ala': 2}),
         FrozenDictionary({'jacek': 0, 'ala': 1})]

s = set(dicts)
print(dicts[0] == dicts[2])
print(dicts[0] != dicts[3])
print(len(s) == 3)
for d in dicts:
    print(d in s)

# Powinno wyświetlić coś w stylu set([{'ala': 4}, {'ala': 1, 'jacek': 0}, {'ala': 2}])
print(s)

#Zadanie 6

class BagOfWords:
    def __init__(self, text):
        self.my_dict = defaultdict(int)
        for w in set(list(text.split(" "))):
            self.my_dict[w] = len(re.findall(w, text))
    def __str__(self):
        return ", ".join(f"{key}: {value}" for key, value in self.my_dict.items())
    def __contains__(self, item):
        return item in self.my_dict.keys()
    def __iter__(self):
        sor = sorted(self.my_dict.items(), key=lambda item: item[1], reverse=True) #krotki
        for key, value in sor:
            yield key
    def __add__(self, other):
        s = ' '.join(k for k, v in self.my_dict.items() for _ in range(v))
        s += ' '
        s += ' '.join(k for k, v in other.my_dict.items() for _ in range(v))
        return BagOfWords(s)
    def __getitem__(self, item):
        return self.my_dict[item]
    def __setitem__(self, key, value):
        self.my_dict[key] = value




bow = BagOfWords("ala ma kota ala ma ala")
print(set(sorted(list("ala ma kota ala ma ala".split(" ")))))
print(dict(bow.my_dict))
print(bow)
for word in bow:
  print(word)
bow1 = BagOfWords("ala ma kota ala ma ala")
bow2 = BagOfWords("tomek tez ma kota")
bow3 = bow1 + bow2
print()
print(bow3)
print(bow1["ala"])
w = "ala ma kota"
print()
