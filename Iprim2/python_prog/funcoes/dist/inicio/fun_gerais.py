#import banco_dados

def rpadagora(l, t):
    r = l
    tagora = float(t)
    r0 = r[str('r0')]
    alfa = r['alfa']
    beta = r['beta']
    t0 = r['t0']
    delt = tagora - t0
    rpad = r0 * (1 + alfa * delt + beta * (delt ** 2))
    return rpad

def inccorr(c, inc):
    c0 = c
    inc0 = inc
    c1 = c0 + inc0
    return c1

def calcv(r, i):
    r0 = r
    i0 = i
    v = r0*i0
    return v

def protrpad(corr, rpad): # rpad é o dicionário com o resistor selecionado. corr é a corrente que vai alimentar este resistor
    corr1 = corr
    rpad1 = rpad
    fat = 1
    while corr1 > rpad1['imax']:
        fat = float(input((f'Esta corrente vai danificar o rasistor padrão {rpad[str(id)]}, digite um fator para reduzir '
              f'a corrente [%]')))
        corr1 = (100-fat)*corr1
    else:
        return corr




'''d = input('digite o resistor')
d = banco_dados.get_res(str(d))
print((rpadagora(d, 23.005)), d['r0'], d['t0'])
#print(ajusfinpjvs(d, 2e-06))'''