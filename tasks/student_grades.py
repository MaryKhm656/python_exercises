"""
Пример работы со словарями
Задача: Сделать вычисления годовых оценок всех студентов класса: найти самых отстающих,
отличников и вычислить средний балл по классу
"""

students = []

try:
    while True:
        student_input = input("Введите имя ученика и его оценку через пробел: ").strip()
        
        if student_input.lower() == 'стоп':
            break
            
        try:
            student_name, student_grade_str = student_input.split(maxsplit=1)
            student_grade = int(student_grade_str)
            students.append({'name': student_name, 'grade': student_grade})
        except ValueError:
            print("Ошибка: некорректный ввод. Нужно ввести имя и оценку через пробел. Пример: 'Иван 5'")
except Exception as error:
    print(f'Ошибка: {error}')
    
if students:
    print("\nСписок всех учеников и их оценок:")
    for student in students:
        print(f"{student['name']}: {student['grade']}")
        
    max_grade = max(students, key=lambda s: s['grade'])['grade']
    print("\nУченики с самой высокой оценкой:")
    for student in students:
        if student['grade'] == max_grade:
            print(f"{student['name']}: {student['grade']}")
            
    min_grade = min(students, key=lambda s: s['grade'])['grade']
    print("\nУченики с самой низкой оценкой:")
    for student in students:
        if student['grade'] == min_grade:
            print(f"{student['name']}: {student['grade']}")
            
    average_grade = sum(s['grade'] for s in students) / len(students)
    print('\nСредний балл по классу: {:.2f}'.format(average_grade))
else:
    print("\nСписок учеников пуст")