import json


def write_order_to_json(item, quantity, price, buyer, date):
    json_data = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', 'r') as json_file:
        json_open = json.load(json_file)
    json_open['orders'].append(json_data)
    with open('orders.json', 'w') as json_file:
        json.dump(json_open, json_file, indent=4)


write_order_to_json('iMac', 2, 300.5, 'Ivan', '12.12.2012')
