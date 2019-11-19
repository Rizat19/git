class A:
    def __init__(meir):
        '''Өзім туралы айтып жатырмын'''
        meir.name='herdftgyhu'
        meir.age='18'
        meir.ar=input('around(Taraz,Almaty,Kyzylorda,Shymkent):')
   
    def hello(a):
        return 'Hello %s'%(a.name)
    
    def old(meir):
        return '\nYour {} years old'.format(2019-int(meir.age))

    def around(s):
        if s.ar=='Taraz':
            return 'Zhambyl oblysynansyn'
        if s.ar=='Almaty':
            return 'Almaty kalasynansyn'
        if s.ar=='Shymkent':
            return 'Shymkent kalasynansyn'
        if s.ar=='Kyzylorda':
            return 'Kyzylorda oblysynansyn'
        
        
        
c=A()
print(c.hello(),c.old(),c.around())
    