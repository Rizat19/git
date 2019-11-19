s={}
while True:
    aty=input('atyndy engiz:')
    if aty=='stop':
        break
    palata=input('sizdin palatanyz:')
    s[aty]=palata
print(s)



while True:
    izdeu=input('siz izdegen adam aty:')
    if izdeu in s:
        print('{} palatasy:'.format(izdeu),s[izdeu])
        break
    
    
        