import math

#x = 250e-6
x = 0.220001e-9
#x2 = format(x, '.8f')
#x3 = ('{:f}'.format(x))
#print(x3)
#print(x, type(x), x2, type(x2))
x4 = str(float(x))
print(x4)
ultimo = len(x4)
pot10 = ''
base = ''
k=int(len(x4))

if 'e' in x4:
    print ('funcionou')

    for i, j in enumerate(x4):
        if j == 'e':
            k = i
        if i > k:
            pot10 += j
    pot10 = int(pot10)
    #print(math.fabs(pot10))


    for i, j in enumerate(x4):
        if i < k:
            base += j
    base = float(base)

else:
    base = float(x4)
    pot10 = int(0)

resultado = str(round(base*10**(pot10), int(math.fabs(pot10))))
n = '.02'
resultado3 = (f'{x:.11f}')
print(resultado3)

#print(resultado3)
#resultado2 = ('{}'.format(x4))
#print(resultado3)

#print(pot10, base, type(base), type(pot10))


'''print(k, type(k))

for i, j in enumerate(x4):
    print(i, j)
    if i > k:
        pot10 += pot10 + j
print(pot10)

#for i, j in enumerate(x4):
#    print(i, j)
    #if j == 'e':
        #print(i, j)'''

