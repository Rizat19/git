san_set=set('0123456789')

while True:
    c=input('input:')
    c_set=set(c)
    if len(c_set-san_set)!=0:
        print('kaita engiz')
    if c =='stop':
        break