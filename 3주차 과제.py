class oil:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print("유종 :", self.name)
        print('리터당 가격 :', self.price,'원')
oil1 = oil('휘발유 :',1535)
oil2 = oil('경유 :',1335)

oil1.info()
oil2.info()