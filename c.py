class F:
    def f(n):
        f=1
        for i in range(n):
            i+=1
            f*=i
        return f
    
    def fi(a):
        f1=f2=1
        i=0
        while i<a-2:
            f=f1+f2
            f1=f2
            f2=f
            i+=1
        return f2