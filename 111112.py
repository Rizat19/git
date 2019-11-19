
import subprocess
asd1=subprocess.check_output(['ls'])
print(asd1.decode('utf-8'))
aty1=subprocess.check_output(['uname'])
print(aty1.decode('utf-8'))
aty=subprocess.check_output(['whoami'])
print(aty.decode('utf-8'))
x = subprocess.check_output(['ifconfig'])
x_dec=x.decode('utf-8')
sp=x_dec.split('\n')
print('PC IP:',sp[17][13:26])

x1= subprocess.check_output(['ip','route'])
x1_dec=x1.decode('utf-8')
sp1=x1_dec.split('\n')
print('\nroute IP:',sp1[0][12:23])

