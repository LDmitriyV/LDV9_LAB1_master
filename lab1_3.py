class Class:
    def __init__(self,x):
        self.x =x
    def lab01(self):

        try:  # Защищенный блок 1
            a = float(input("Введите A= "))
            b = float(input("Введите B= "))
            y = (5 * a * b) / (pow(x1, 2) + pow(a, 2))
        except:
            print("Ошибка данных")
        print("y = %.1f" % y)

    def lab01_2(self):
        a = float(input("Введите A= "))
        b = float(input("Введите B= "))
        y = 4 * (pow((a + b - x1), 2))
        print("y = %.1f" % y)

if __name__ == '__main__':
    while True:
        x1 = float(input("Введите X = "))
        if x1 <=5:
            up = Class(x1)
            up.lab01()
        elif x1 > 5:
            up = Class(x1)
            up.lab01_2()
        input("Нажмите Enter для выхода")
        quit()
