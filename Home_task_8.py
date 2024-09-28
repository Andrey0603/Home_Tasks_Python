# Задание 1. Работа с основными данными
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
# pickle. Для дочерних объектов указывайте родительскую директорию. Для
# каждого объекта укажите файл это или директория. Для файлов сохраните его
# размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами разных форматов

import os
import json
import csv
import pickle
def get_size(path):

    if os.path.isfile(path):

        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0

        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size
def traverse_directory(directory):

    result = []


    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)

            result.append({
                'name': name,
                'path': path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
            })
    return result
def save_to_json(data, filename):

    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
def save_to_csv(data, filename):

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'path','type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)
def save_to_pickle(data, filename):

    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
def main(directory):

    data = traverse_directory(directory)
    save_to_json(data, 'directory_info.json')
    save_to_csv(data, 'directory_info.csv')
    save_to_pickle(data, 'directory_info.pkl')
if __name__ == "__main__":

    main('your_directory')
    

# Задача 2. Объединение данных из нескольких JSON файлов
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов.    

import json
import glob
def merge_json_files(input_files, output_file):

    merged_data = [] 
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f) 
                merged_data.extend(data) 
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON файла: {file}")
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4) 
if __name__ == "__main__":

    json_files = glob.glob('employees*.json')
    merge_json_files(json_files, 'all_employees.json')
    
# Задача 3. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
# файл. JSON файл содержит данные о продуктах (название, цена, количество на
# складе). В CSV файле каждая строка должна соответствовать одному продукту.
# Пример: Из файла products.json нужно создать products.csv.
    
import json
import csv
def json_to_csv(json_file, csv_file):

    with open(json_file, 'r') as f:
        data = json.load(f) 

    if not isinstance(data, list) or not all(isinstance(item, dict)
for item in data):
        raise ValueError("Некорректный формат данных в JSON файле")

    with open(csv_file, 'w', newline='') as f:
        fieldnames = data[0].keys() 
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader() # Запись заголовков
        writer.writerows(data) # Запись данных
if __name__ == "__main__":
    json_to_csv('products.json', 'products.csv')
    
# Задача 4. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из CSV файла, содержащего
# информацию о продажах (название продукта, количество, цена за единицу), и
# подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
# новом CSV файле.
# Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
# продукта будет указана общая выручка.    

import csv
def calculate_total_sales(input_file, output_file):
    sales_totals = {} 

    with open(input_file, 'r') as f:    
        reader = csv.DictReader(f)
        for row in reader:
            product = row['название продукта']
            quantity = int(row['количество']) 
            price_per_unit = float(row['цена за единицу']) 
            total_sales = quantity * price_per_unit 
            if product in sales_totals:
                sales_totals[product] += total_sales 
            else:
                sales_totals[product] = total_sales 
    with open(output_file, 'w', newline='') as f:
        fieldnames = ['название продукта', 'общая выручка']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for product, total_sales in sales_totals.items():
            writer.writerow({'название продукта': product, 'общая выручка': total_sales})
if __name__ == "__main__":
    calculate_total_sales('sales.csv', 'total_sales.csv')
    
    
# Задача 5. Конвертация CSV в JSON с изменением структуры данных
# Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
# JSON файл с другой структурой. CSV файл содержит данные о книгах (название,
# автор, год издания). В JSON файле данные должны быть сгруппированы по
# авторам, а книги каждого автора должны быть записаны как список.
# Пример: Из файла books.csv нужно создать файл books_by_author.json, где
# книги сгруппированы по авторам.


import csv
import json
def convert_csv_to_json(input_file, output_file):
    books_by_author = {} 
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }
        if author in books_by_author:
            books_by_author[author].append(book) 
        else:
            books_by_author[author] = [book] 

    with open(output_file, 'w') as f:
        json.dump(books_by_author, f, indent=4) 
if __name__ == "__main__":
    convert_csv_to_json('books.csv', 'books_by_author.json')
