import funcoes.inicio

while True:
    a = funcoes.inicio.comeco()
    if a == 4:
        break
    elif a == 1:
        print('func1')
    elif a == 2:
        print('func2')
    elif a == 3:
        print('func3')
    else:
        print('digite uma opçao valida')

print('sistema encerrado')



