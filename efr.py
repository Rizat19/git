s1={}
s={}
class H:
    
    def ter(s):
        print('terapia bolimi')
        print(s)
        palata=input('sizdin palatanyz:')
        s1[s]=palata
        print(s1)
    def stomac(d):
        print('stomatologia bolimi')
        print(d)
        palata=input('sizdin palatanyz:')
        s[d]=palata
        print(s)
        
    def registr(n):
        while True:#пациенттер
            n=input('atyn kim?')
            if n=='stop':
                break
            a=input('senin kai zherin auyryp tur?(bas / tis):')
            if a=='bas':
                print('sen terapia bolimine bar!')
                H.ter(n)
            if a=='tis':
                print('sen stomatologia bolimine bar!')
                H.stomac(n)
        


    def registr_izdeu(i):
        while True:
            izdeu=input('siz izdegen adam aty:')
            if izdeu in s1:
                print('{} terapia boliminde, palatasy :'.format(izdeu),s1[izdeu])
                break
            elif izdeu in s:
                print('{}  stomatologia boliminde, palatasy :'.format(izdeu),s[izdeu])
                break
            else:
                print('Bul bolnicada ondai adam jok!')
c=H()
c.registr()            
c.registr_izdeu()    
##
##c=H()
##c.registr()


