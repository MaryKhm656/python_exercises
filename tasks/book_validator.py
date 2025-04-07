"""
Проверка данных о книге, с использованием match/case
Ожидаемый формат ввода: id, автор, название[, цена, год]
Примеры:
1,Толстой,Война и мир,899.99,2022
2,Пушкин,Евгений Онегин
3,Булгаков,Мастер и Маргарита,700.00
"""

t = (int, str, str, float, int)

user_input = input("Введите данные о книге через запятую (id, автор, название [, цена, год]): ")

try:
    data = user_input.split(",")
    
    if len(data) < 3:
        raise ValueError("Недостаточно данных. Нужно минимум: id, автор, название")
    
    book = [t[i](x.strip()) if t[i] != str else x.strip() for i, x in enumerate(data)]
    
    match book:
        case [_, author, title] if len(author) >= 6 and len(title) >= 10:
            print("Книга прошла проверку по длине автора и названия")
        case [_, author, title, price] if len(author) >= 6 and price > 0:
            print("Книга прошла проверку по длине автора и положительной цене")
        case [_, author, title, _, year] if year > 2020:
            print("Книга прошла проверку по году выпуска")
        case [_, author, title, price, year] if price > 0 and year >= 2020:
            print("Книга прошла проверку по цене и году выпуска")
        case _:
            print("Книга не прошла проверку — условия не соблюдены")
            
except ValueError as e:
    print(f"Ошибка {e}")
except IndexError as e:
    print("Ошибка: недостаточно данных для сопоставления")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")