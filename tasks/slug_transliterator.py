# Генерация "чпу-строки" (slug) из заголовка на кириллице
# Преобразует кириллические символы в латинские по таблице транслитерации
# Все пробелы и знаки препинания заменяются на дефисы
# Удаляются дублирующиеся дефисы и дефисы в начале/конце строки
#
# Примеры:
# "Я супер кодер"           -> ya-super-koder
# "Привет, мир!!!"          -> privet-mir
# "Python и код"            -> python-i-kod
# "  Много   пробелов  "    -> mnogo-probelov
# "C# & SQL!!!"             -> c-sql

import  re

cyrillic_to_latin = [
    'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i','y', 'k', 'l', 'm', 'n', 'o',
    'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'shch', '', 'y', '',
    'e', 'yu', 'ya'
]

start_index = ord('а')
title = input("Введите заголовок: ").strip()
slug = ''

for char in title.lower():
    if 'а' <= char <= 'я':
        slug += cyrillic_to_latin[ord(char) - start_index]
    elif char == 'ё':
        slug += 'yo'
    elif char in ' !?;:.,':
        slug += '-'
    elif char.isalnum():
        slug += char
    else:
        slug += '-'
        
slug = re.sub('-{2,}', '-', slug)

slug = slug.strip('-')

print(slug)