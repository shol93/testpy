import random

num_tickets = int(input("Количество проданных билетов: "))
bus_capacity=20 # Кол-во мест в автобусе

bus_quantity=num_tickets//bus_capacity # Полный автобус
num_tickets=num_tickets%bus_capacity # Ост. пассажиры

has_partial_bus=False
empty_seats=0

if num_tickets>=bus_capacity/2:
    bus_quantity+=1
    has_partial_bus=True
    empty_seats=bus_capacity-num_tickets
    num_tickets=0

    



print(bus_quantity, num_tickets, has_partial_bus, empty_seats)
