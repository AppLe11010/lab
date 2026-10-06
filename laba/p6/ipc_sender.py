import posix_ipc
import time

QUEUE_NAME = "/sys_prog_queue"

print("Отправитель - Обращаемся к ядру для создания очереди...")
mq = posix_ipc.MessageQueue(QUEUE_NAME, flags=posix_ipc.O_CREAT, mode=0o666)

print(f"Отправитель - Системная очередь успешно инициализирована: {QUEUE_NAME}")

for i in range(1, 6):
    message = f"Message ID {i} payload"
    binary_data = message.encode('utf-8')
    print(f"\[ОТПРАВИТЕЛЬ\] Выполняем mq\_send: отправка '{message}' в буфер ядра...")  
    mq.send(binary_data)  
    time.sleep(0.5)
print("[ОТПРАВИТЕЛЬ] Все сообщения отправлены в Ring 0. Завершение работы.")
mq.close()