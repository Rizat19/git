class Tax():
    san_set = set('.0123456789')
    z = []
    while True:
        Tax.zarplata = input("1 айда шарт бойынша қанша айлық алу керексің?:\n")
        Tax.zarplata_set = set(Tax.zarplata)
        if len(zarplata_set - san_set) == 0:
            z.append(Tax.zarplata)
            break
        else:
            print('kaita engiz!')
    Tax.opv =  float(Tax.zarplata)* 0.1
    Tax.ipn = (float(Tax.zarplata) - Tax.opv - 42500) * 0.1
    Tax.taza_tabys = float(Tax.zarplata) - (Tax.opv + Tax.ipn)
    print('Ал сен 1-айдағы таза табысың:%d' % (Tax.taza_tabys))
    Tax.so = (float(Tax.zarplata) - Tax.opv) * 0.035
    Tax.n = (float(Tax.zarplata)- Tax.opv) * 0.095-Tax.so
    Tax.med_strahovka = float(Tax.zarplata) * 0.015
    Tax.compania_nalog = Tax.so + Tax.sn + Tax.med_strahovka

    def fiz():
        print('сенің шарт бойынша алу керек айлығың:', float(Tax.zarplata))
        print('Ал сен 1-айдағы таза табысың:%d' % (Tax.taza_tabys))
        print('Компания налогы:%d,'
              ' ОПВ:%d, '
              'ИПН:%d' % (Tax.compania_nalog,Tax.opv, Tax.ipn))
##    def ur(s):
##        s.tabys = input('Компанияның 1-айдағы табысы қанша?')
##        s.shygys = input('Компанияның 1-айдағы шығысы қанша?')
##        tab = float(s.tabys)
##        shygys1 = float(s.shygys)
##        nalog1 = tab * 0.03
##        nalog2 = (tab - shygys1) * 0.1
##
##        taza_shygyn = nalog1 + nalog2 +ri.zarplata+ri.compania_nalog+ shygys1
##        print(taza_shygyn)
##        taza_tabys=tab-taza_shygyn
##        print(taza_tabys)

c=Tax()
c.fiz()
