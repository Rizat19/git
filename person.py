class F:
    def fact():
        n=int(input('n:'))
        f=1
        for i in range(1,n+1):
            f*=i
        return f   
    def fib():
        a=int(input('n:'))
        f1=f2=1
        i=0
        while i<a-2:
            g=f1+f2
            f1=f2
            f2=g
            i+=1
        return g







