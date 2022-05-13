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
    print(a)
    print(b)
    if a != () and b != {}:
        return type(a) and type(b)
    else:
        return 'list and dictionary (array and hash in perl) noy full'
    # return type(a)  type(b)


dics = {'f': 5, 'r': 6}
print(add_ints(*(3, 4), **dics))

cooler_add_ints = document_it(add_ints)
cooler_add_ints(*(3, 4),**{'f': 5, 'r': 6})
