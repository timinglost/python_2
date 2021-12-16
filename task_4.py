original_str_item = ['разработка', 'сокет', 'декоратор', 'protocol', 'standard']
str_item_bytes = []
new_str_item = []

for i in original_str_item:
    item_bytes = i.encode('utf-8')
    str_item_bytes.append(item_bytes)

for i in str_item_bytes:
    item_bytes = i.decode('utf-8')
    new_str_item.append(item_bytes)

print('str_item_bytes:')

for i in str_item_bytes:
    print(i)

print('new_str_item:')

for i in new_str_item:
    print(i)

"""
str_item_bytes:
    b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
    b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
    b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
    b'protocol'
    b'standard'
new_str_item:
    разработка
    сокет
    декоратор
    protocol
    standard
"""
