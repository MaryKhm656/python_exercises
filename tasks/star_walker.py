"""
Мини-игра для демонстрации работы с циклами, матрицами и match/case
"""

field = [['.' for _ in range(10)] for _ in range(10)]
player_x, player_y = 5, 5
field[player_x][player_y] = '*'

def print_field(field):
    for row in field:
        print(' '.join(map(str, row)))
    print()
    
while True:
    print_field(field)
    direction = input("Введите направление (W/A/S/D) или 'Q' для выхода: ").strip().lower()
    
    if direction == 'q':
        print("Игра завершена!")
        break
        
    old_x, old_y = player_x, player_y
    
    try:
        field[player_x][player_y] = '.'
        
        match direction:
            case 'w':
                player_x -= 1
            case 's':
                player_x += 1
            case 'd':
                player_y += 1
            case 'a':
                player_y -= 1
            case _:
                print("Некорректный ввод! Используйте W/A/S/D или Q для выхода")
                field[player_x][player_y] = '*'
                continue
                
        if not (0 <= player_x < 10) or not (0 <= player_y < 10):
            raise IndexError("Выход за границы поля!")
        
        field[player_x][player_y] = '*'
        
    except IndexError:
        print("Ошибка: нельзя выйти за границы поля!")
        player_x, player_y = old_x, old_y
        field[player_x][player_y]
        
