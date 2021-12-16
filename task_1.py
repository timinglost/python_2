str_item = ['разработка', 'сокет', 'декоратор']

print('str_item:')

for i in str_item:
    print(type(i), i)

print('str_item_unicode:')

str_item_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    ]

for i in str_item_unicode:
    print(type(i), i)
"""
str_item:
    <class 'str'> разработка
    <class 'str'> сокет
    <class 'str'> декоратор
str_item_unicode:
    <class 'str'> разработка
    <class 'str'> сокет
    <class 'str'> декоратор
"""
