import glob
import csv


def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    count_file = len(glob.glob('info_*.txt'))
    for i in range(count_file):
        with open(f'info_{i + 1}.txt', 'r') as info:
            for line in info:
                if 'Изготовитель системы' in line:
                    os_prod_list.append(' '.join(line.split()[2:]))
                if 'Название ОС' in line:
                    os_name_list.append(' '.join(line.split()[2:]))
                if 'Код продукта' in line:
                    os_code_list.append(' '.join(line.split()[2:]))
                if 'Тип системы' in line:
                    os_type_list.append(' '.join(line.split()[2:]))
    for i in range(count_file):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


def write_to_csv():
    csv_data = get_data()
    with open('task_1_csv.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in csv_data:
            csv_writer.writerow(row)


write_to_csv()
