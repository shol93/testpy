import random

print(f"Выбирите место куда хотите отправиться : \nМосква, \nПитер, \nЕкатеринбург, \nКраснодар.")
location=input()

if location=="Москва":
    bus_capacity=50
elif location=="Питер":
    bus_capacity=40
elif location=="Екатеринбург":
    bus_capacity=30
elif location=="Краснодар":
    bus_capacity=20

else:
    print("Неверно введены значения!!!")
    exit()


num_tickets = int(input("Количество проданных билетов: "))
print("Всего мест в автобусе: ", bus_capacity)

full_bus_capacity = num_tickets // bus_capacity
num_tickets_left = num_tickets % bus_capacity
print(f"Заполнено автобусов: {full_bus_capacity}\nОсталось: {num_tickets_left}")
