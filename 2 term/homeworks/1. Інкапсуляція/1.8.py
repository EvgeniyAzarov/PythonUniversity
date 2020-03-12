class Passenger:
    def __init__(self, start, end, dist, km_price):
        self._start = start
        self._end = end
        self._dist = dist
        self._km_price = km_price

    def calculate_price(self):
        return self.dist * self._km_price

    def get_info(self):
        return 

with open("passengers.txt") as f:
    for line in f:
        p = Passenger(line.split())
        print(p.calculate_price())
