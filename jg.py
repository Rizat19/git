san_set=set('.0123456789')
d=[]
while True:
    c=input("> ")
    c_set=set(c)
    print(c_set)
    print(len(c_set))
    if len(c_set-san_set)!=0:
        print('kaita engiz:')
    if c in 'stop':
        break
    
    