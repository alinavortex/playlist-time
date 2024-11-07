## project_1

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * список из кортежа строк и кортежа вещественных чисел 
#   * многострочная строка 
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

import random
from datetime import timedelta

playlist_d = [
    ("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
    (5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
]

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""
def get_duration(playlist):
    return playlist.items()
merge_playlist = list(zip(playlist_d[0], playlist_d[1]))
random.shuffle(merge_playlist)

def get_playlist_duration_string(playlist, n):
    #разделияем строку на строки и фильтруем пустые строки
    lines = [line.strip() for line in playlist.strip().split('\n') if line.strip()]
    #список длительностит песен
    song_durations = []
    for line in lines:
        try:
            #извлекаем длительнось песни в конце каждой стр
            duration = float(line.split()[-1])
            song_durations.append(duration)
        except ValueError:
            #если длительность не распознана - пропускаем
            continue
    #случайным образом выбираем n песен
    chosen_songs_indices = random.sample(range(len(song_durations)), n)
    #подсчет общ времени
    total_duration = sum(song_durations[i] for i in chosen_songs_indices)
    return total_duration

#объединяем плейлисты
def get_duration(playlist, n):
    if isinstance(playlist, tuple):
        #плейлист кортеж
        total_duration = get_playlist_duration_tuple(playlist_d, n)
    elif isinstance(playlist_d, str):
        #плейлист многострочный
        total_duration = get_playlist_duration_string(playlist_e, n)
    else:
        raise TypeError("Неподдерживаемый формат плейлиста")
    
    #преобразуем время в объект timedelta
    total_duration_timedelta = timedelta(minutes=total_duration)

    #возвращаем результат как объект timedelta
    return total_duration_timedelta

