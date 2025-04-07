"""
 Подсчёт результатов матчей между командами
 Формат ввода:
   Сначала вводится число n — количество матчей.
   Затем n строк с данными о каждом матче: команда1;счёт1;команда2;счёт2
 Пример ввода:
   3
   Спартак;3;Зенит;1
   Зенит;2;Спартак;2
   ЦСКА;0;Спартак;1
"""

def main():
    try:
        num_matches = int(input("Введите количество матчей: "))
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    results = {}

    for i in range(num_matches):
        try:
            match_data = input(f"Введите результат матча {i+1}: ").split(';')
            if len(match_data) != 4:
                raise ValueError("Неверное количество данных. Нужно 4 значения.")

            team1, score1, team2, score2 = match_data
            score1 = int(score1)
            score2 = int(score2)

        except ValueError as e:
            print(f"Ошибка в данных матча: {e}")
            return

        for team in (team1, team2):
            if team not in results:
                results[team] = {
                    'games': 0,
                    'wins': 0,
                    'draws': 0,
                    'losses': 0,
                    'points': 0
                }

        results[team1]['games'] += 1
        results[team2]['games'] += 1

        if score1 > score2:
            results[team1]['wins'] += 1
            results[team1]['points'] += 3
            results[team2]['losses'] += 1
        elif score1 < score2:
            results[team2]['wins'] += 1
            results[team2]['points'] += 3
            results[team1]['losses'] += 1
        else:
            results[team1]['draws'] += 1
            results[team2]['draws'] += 1
            results[team1]['points'] += 1
            results[team2]['points'] += 1

    print("\nИтоговая таблица:")
    for team, stats in results.items():
        print(f"{team}: {stats['games']} {stats['wins']} {stats['draws']} {stats['losses']} {stats['points']}")

if __name__ == "__main__":
    main()
