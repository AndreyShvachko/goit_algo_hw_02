import queue
import random
import time

# Створюємо чергу заявок
request_queue = queue.Queue()

# Лічильник для унікальних ідентифікаторів заявок
request_counter = 0

# Функція генерації нових заявок
def generate_request():
    global request_counter
    request_counter += 1
    request = f"Request #{request_counter}"
    request_queue.put(request)
    print(f"Заявка додана: {request}")

# Функція обробки заявок
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробка {request}")
        time.sleep(2)  # Імітація часу обробки
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
def main():
    try:
        while True:
            # Імітація генерації нових заявок випадковим чином
            if random.random() < 0.5:
                generate_request()
            process_request()

            # Пауза між ітераціями
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nПрограма завершена.")

if __name__ == "__main__":
    main()

