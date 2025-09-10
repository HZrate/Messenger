import socket # Импорт библеотеки
import var # Импорт переменных

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Настраиваем
s.connect(((var.ip), int(var.port))) # Подключаемся к нашему серверу.

while True: #Цикл повторений для отправки 1+ сообщений
    message = input() # Ввод сообщения
    s.sendall((message).encode(var.encode)) # Отправляем фразу.
    data = s.recv(1024) # Получаем данные из сокета.