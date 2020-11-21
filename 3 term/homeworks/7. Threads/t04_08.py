# Є готель з N номерами. Через випадковий час від 1 до t1 приходить
# новий клієнт та заселяється у один з номерів (якщо є вільний), у якому живе
# час від 1 до t2. Якщо вільних номерів немає, то клієнт очікує на звільнення
# будь-якого номера. При заданих параметрах N, t1, t2 розрахувати середню
# довжину черги клієнтів та середній час очікування.
# Вказівка: один клієнт – це 1 потік.

from threading import Thread
from queue import Queue
from time import time, sleep
from collections import namedtuple
import random
import logging

logging.basicConfig(level=logging.DEBUG)

N = 4
living_time_min = 10
living_time_max = 20
arrive_time_min = 1
arrive_time_max = 4

Client = namedtuple("Client", "index living_time")
hotel = Queue(maxsize=N)
queue = Queue()


def reseption():
    while True:
        client = queue.get()
        # logging.debug("Client {} is ready to check in".format(client.index))    
        hotel.put(client)
        logging.debug("Client {} checked in".format(client.index))    
        
        client_th = Thread(target=client_proc, args=(client, ), daemon=True) 
        client_th.start()


def client_proc(client: Client):
    sleep(client.living_time) 
    hotel.get() 
    # In reality client with some other index checked out
    # because of queue usage
    logging.debug("Client {} checked out".format(client.index))


def client_generator():
    client_index = 0
    while True:
        arrive_time = \
            (random.random() * (arrive_time_max - arrive_time_min) + arrive_time_min)
        living_time = \
            (random.random() * (living_time_max - living_time_min) + living_time_min)
        
        sleep(arrive_time)
        queue.put(Client(client_index, living_time))
        logging.debug("Client {} queued".format(client_index))
        client_index += 1
    
    
count = 1
ssum = 0
def statistic():
    global count
    global ssum
    while True:
        ssum += queue.qsize()
        count += 1
        sleep(0.1)
       

if __name__ == '__main__':
    try:
        reseption_th = Thread(target=reseption, daemon=True)
        client_generator_th = Thread(target=client_generator, daemon=True)
        statistic_th = Thread(target=statistic, daemon=True)
        
        client_generator_th.start()
        reseption_th.start()
        statistic_th.start()
        
        statistic_th.join()
    except KeyboardInterrupt:
        print("Mean number of persons in queue: {}".format(ssum / count))
     
