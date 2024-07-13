team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 6
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

challenge_result = 'Ничья' if score_1 == score_2 else (team1_name if score_1 > score_2 else team2_name)

print('В команде Мастера кода участников: %s' % team1_num)
print('В команде Мастера кода участников: %s и %s' % (team1_num, team2_num))

print('Команда Волшебники данных решила задач: {}\nВолшебники данных решили задачи за: {}c'.format(score_2, team2_time))

print(f'Команды решили {score_1} и {score_2} задач')

print(f'Результат битвы: победа команды {challenge_result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.')
