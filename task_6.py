from chardet.universaldetector import UniversalDetector

print('кодировка файла по умолчанию:')

detector = UniversalDetector()
with open('test_file.txt', 'rb') as test_file:
    for line in test_file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)

print('файл в формате Unicode:')
with open('test_file.txt', encoding='utf-8', errors='replace') as test_file:
    for line in test_file:
        print(line)

"""
кодировка файла по умолчанию:
    {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
файл в формате Unicode:
    сетевое программирование
    
    сокет
    
    декоратор
"""
