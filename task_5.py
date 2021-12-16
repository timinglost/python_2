import subprocess

print('yandex.ru:')

args = ['ping', 'yandex.ru']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)


for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))

print('youtube.com:')

args = ['ping', 'youtube.com']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)


for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))

"""
yandex.ru:
    
    
    Обмен пакетами с yandex.ru [2a02:6b8:a::a] с 32 байтами данных:
    
    Ответ от 2a02:6b8:a::a: время=7мс 
    
    Превышен интервал ожидания для запроса.
    
    Ответ от 2a02:6b8:a::a: время=10мс 
    
    Ответ от 2a02:6b8:a::a: время=217мс 
    
    
    
    Статистика Ping для 2a02:6b8:a::a:
    
        Пакетов: отправлено = 4, получено = 3, потеряно = 1
    
        (25% потерь)
    
    Приблизительное время приема-передачи в мс:
    
        Минимальное = 7мсек, Максимальное = 217 мсек, Среднее = 78 мсек

youtube.com:
    
    
    Обмен пакетами с youtube.com [2a00:1450:4010:c01::5b] с 32 байтами данных:
    
    Ответ от 2a00:1450:4010:c01::5b: время=22мс 
    
    Ответ от 2a00:1450:4010:c01::5b: время=466мс 
    
    Ответ от 2a00:1450:4010:c01::5b: время=24мс 
    
    Ответ от 2a00:1450:4010:c01::5b: время=368мс 
    
    
    
    Статистика Ping для 2a00:1450:4010:c01::5b:
    
        Пакетов: отправлено = 4, получено = 4, потеряно = 0
    
        (0% потерь)
    
    Приблизительное время приема-передачи в мс:
    
        Минимальное = 22мсек, Максимальное = 466 мсек, Среднее = 220 мсек
"""
