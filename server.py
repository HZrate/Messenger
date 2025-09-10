import socket # Импорт библеотеки
import var # Импорт переменных

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Настройки
s.bind(((var.ip), int(var.port))) # Привязываем серверный сокет к localhost и 5030 порту.
s.listen(1) # Начинаем прослушивать входящие соединения.
conn, addr = s.accept() # Метод который принимает входящее соединение.

while True: # Цикл повторения для 1+ сообщений
	data = conn.recv(1024) # Получаем данные из сокета.
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode(var.encode)) # Вывод данных