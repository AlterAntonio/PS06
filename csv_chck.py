import csv

def read_csv_file(path):
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # Пропуск строки с заголовками

        for row in reader:
            print(f"Наименование товара: {row[0]}")
            print(f"Цена товара: {row[1]}")
            print(f"Ссылка на страницу с товаром: {row[2]}")
            print("-" * 40) # Разделитель для удобства

path = r'rozetka_csv/rozetka_csv/spiders/rztk.csv'
read_csv_file(path)