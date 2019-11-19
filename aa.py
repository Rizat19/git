class A:
    def __init__(self):
        self.f=input('напишите цифры через пробел:')
    def su(self):
        q=set('abcdefghigklmnopqrstuvwxyz!@#$%^&*()_+|/*-+~":?;')
        f1=(self.f).split()
##        print(f1)
        sum=0
        for i in f1:
            for item in i:
                if item in q:
                    print('qate')
            if i not in q:
                sum+=int(i)
            
                    
        print('сумма только цифров:',sum)
                
            
cl=A()
cl.su()