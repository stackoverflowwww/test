class oil:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print("���� :", self.name)
        print('���ʹ� ���� :', self.price,'��')
oil1 = oil('�ֹ��� :',1535)
oil2 = oil('���� :',1335)

oil1.info()
oil2.info()