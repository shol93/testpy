import random

rand_num = random.randint(22, 48)

num_tickets = int(input("Количество проданных билетов: "))
print("Всего мест в автобусе: ", rand_num)
bus_capacity = rand_num

full_bus_capacity = num_tickets // bus_capacity
num_tickets_left = num_tickets % bus_capacity
print(f"Заполнено автобусов: {full_bus_capacity}\nОсталось: {num_tickets_left}")
