import yaml


content = {
    'item': ['item-1', 'item-2'],
    'price': 100,
    'some_price': {
        'price-1': '1€',
        'price-2': '1€',
        'price-3': '1€',
        'price-4': '1€'
    }
}
with open('file.yaml', 'w') as yaml_file:
    yaml.dump(content, yaml_file, default_flow_style=False, allow_unicode = True)

with open('file.yaml', 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.Loader)
    print(yaml_data)
"""
Данные совподают:
    {'item': ['item-1', 'item-2'], 
    'price': 100, 
    'some_price': {'price-1': '1€', 
                    'price-2': '1€', 
                    'price-3': '1€', 
                    'price-4': '1€'}}
"""
