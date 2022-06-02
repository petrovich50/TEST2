print('Hello test.py')
f = r'fgfggfgf'
f.index('fgg', 0, 20)
if f in 'fgfgggf':
    print('YES!')
else:
    print('NO')

a = 'zyxwvutsrqponmlkjihgfedcba'
a = a[::-1]
print(len(a))
print(a.split())
list = []
dict = {}
for i in range(0, len(a)):
    list.append(a.__getitem__(i))
    dict[i] = a.__getitem__(i)

print(list)
print(dict)
print('::'.join(list))
str = 'a famous duck goes into a famous bar...'
print(str.replace('a', 'a famous', 100))
import unicodedata

print(unicodedata.name('\u20ac'))
print(unicodedata.lookup(unicodedata.name('\u20ac')))
print(' earth k))!)'.strip(')!'))
import string

prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))
print(string.whitespace + string.punctuation)
print('%s' % 7.03)
cat = 'Chester'
actor = 'Richard Gere'
weight = 28
print("Our cat %s weighs %s pounds" % (cat, weight))


def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


@document_it
def add_ints(*a, **b):
    '''This is function that will be decarated with anoether one
    function mashala'''
    print(a)
    print(b)
    if a != () and b != {}:
        return type(a) and type(b)
    else:
        print('My TUTA')
        return add_ints.__name__
    # return type(a)  type(b)


cooler_add_ints = document_it(add_ints)
cooler_add_ints(*(3, 4))
print('------\n\n')
dics = {'f': 5, 'r': 6}
print(add_ints(*(3, 4)))


class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        ...
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(third == first)
print(repr(first))


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('\u0115')
# print('THIS IS A ','\N{LATIN SMALL LETTER ESH}',' LETTER')
# fin = open('bfile', 'rb')
# d = fin.read()

import locale
from datetime import date

halloween = date(2019, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B %d')
