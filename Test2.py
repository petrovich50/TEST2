import locale
from datetime import date

halloween = date(2019, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is','ru_ru']:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))

#print(locale.getlocale(category=locale.LC_ALL))

import os
os.getgid()