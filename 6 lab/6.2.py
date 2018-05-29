class rast(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def jopa(self):
        if (x1 == x2) and (x1 == y2) and (x1 == y1):
            return "Это является квадратом"
        if not ((x1 == x2) and (x1 == y2) and (x1 == y1)):
            return "Это не является квадратом"


x1 = int(input("Введите X1: "))
y1 = int(input("Введите Y1: "))
x2 = int(input("Введите X2: "))
y2 = int(input("Введите Y2: "))


rast = rast(x1, y1, x2, y2)

print(rast.jopa())
