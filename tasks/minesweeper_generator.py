"""
Генератор поля для игры "Сапёр"

Программа создаёт игровое поле для "Сапёра" на основе введённых данных:
1. Первая строка ввода: количество строк, столбцов и мин
2. Последующие строки: координаты мин (строка, столбец)
3. Вывод: игровое поле с минами (*) и числами, указывающими количество мин вокруг клетки
"""

def main():
    try:
        print("Введите количество строк, столбцов и мин через пробел:")
        rows, cols, mines = map(int, input().split())

        if rows <= 0 or cols <= 0 or mines < 0:
            raise ValueError("Размеры должны быть положительными, а количество мин - неотрицательным")
        if mines > rows * cols:
            raise ValueError("Слишком много мин для указанного размера поля")

        field = [[0 for _ in range(cols)] for _ in range(rows)]

        print(f"\nВведите координаты {mines} мин (номер строки и столбца от 1 до {rows} и от 1 до {cols}):")
        mines_placed = 0
        while mines_placed < mines:
            try:
                row, col = map(int, input().split())
                if not (1 <= row <= rows) or not (1 <= col <= cols):
                    raise ValueError(f"Координаты должны быть от 1 до {rows} для строк и от 1 до {cols} для столбцов")
                if field[row-1][col-1] == -1:
                    print("Внимание: мина уже есть в этой позиции")
                    continue
                field[row-1][col-1] = -1
                mines_placed += 1
            except ValueError as e:
                print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте ещё раз.")
                continue
        
        for i in range(rows):
            for j in range(cols):
                if field[i][j] == -1:
                    continue

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and field[ni][nj] == -1:
                            field[i][j] += 1

        print("\nСгенерированное поле для игры 'Сапёр':")
        for row in field:
            for cell in row:
                if cell == -1:
                    print(' * ', end='')
                elif cell == 0:
                    print(' . ', end='')
                else:
                    print(f' {cell} ', end='')
            print()

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()