class H():
##    def __init__(self):
##        self.a=input('senin kai zherin auyryp tur?(bas / tis:')
    def ter(s):
        print('\n',s,'sen terapia boliminde emdelu kereksiz,sizdi spisokka engizemiz')
        
    def stomac(d):
        print('\n',d,'sen stomatologia boliminde emdelu kereksiz,sizdi spisokka engizemiz')
        
    def registr(n):
        n=input('atyn kim?')
        a=input('senin kai zherin auyryp tur?(bas / tis):')
        if a=='bas':
            print('sen terapia bolimine bar!')
            return H.ter(n)
        if a=='tis':
            print('sen stomatologia bolimine bar!')
            return H.stomac(n)
        

c=H()
c.registr()


