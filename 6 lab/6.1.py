class rast(object):

    def __init__(self, x,y):
        self.x = x
        self.y = y
    def jopa(self):
        self.x *= 60
        self.ggg = self.x * self.y
        return self.ggg


x = int(input("Введите скорость в м/с: "))
y = int(input("Введите Время в мин: "))


rast = rast(x,y)

print("Пройденное растояние в метрах= ", rast.jopa())