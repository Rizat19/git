class A:
    def __init__(self):
        self.f=input('напишите цифры через пробел:')
    def su(self):
        f1=(self.f).split()
        print(f1)
        sum=0
        for i in f1:
            sum+=int(i)
        print('сумма этих цифров:',sum)
cl=A()
cl.su()