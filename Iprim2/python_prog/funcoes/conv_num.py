def scipara5730(a = list()):
    b = a
    local_list = []
    for i, j in enumerate(b):
        #print(i, j)
        comando = str('OUT ' + (f'{j:.7f} ') + 'A')
        local_list.insert(i, comando)
    return(local_list)

def scipara5730b(a):
    corrarred = a
    #b = str(a)
    if corrarred < 220e-6:
        corrarred = round(corrarred, 10)
    elif corrarred < 2.2e-3:
        corrarred = round(corrarred, 9)
    elif corrarred < 22e-3:
        corrarred = round(corrarred, 8)
    elif corrarred < 220e-3:
        corrarred = round(corrarred, 7)
    elif corrarred < 2200e-3:
        corrarred = round(corrarred, 6)
    b = str(corrarred)
    comando = str('OUT ' + b + 'A')
    return comando

def prefi(a = list()):
    b = a
    local_list2 = []
    local_list3 = []
    for i, j in enumerate(b):
        print(i,j)
        if j/(10**(-9))>1:
            valcon = j/(10**(-9))
            pref = 'n'
        if j/(10**(-6))>1:
            valcon = j/(10**(-6))
            pref = 'μ'
        if j / (10 ** (-3)) > 1:
            valcon = j / (10 ** (-3))
            pref = 'm'
        local_list3 = [valcon, pref]
        local_list2.insert(i, local_list3)
    return local_list2

def prefi2(a, c=0):
    b = a
    if b / (10 ** (-12)) > 1:
        valcon2 = round(b / (10 ** (-12)), c+ 12)
        pref = 'p'
    if b / (10 ** (-9)) > 1:
        valcon2 = round(b / (10 ** (-9)), c + 9)
        pref = 'n'
    if b / (10 ** (-6)) > 1:
        valcon2 = round(b / (10 ** (-6)), c + 6)
        #pref = 'μ'
        pref = 'u'
    if b / (10 ** (-3)) > 1:
        valcon2 = round(b / (10 ** (-3)), c + 3)
        pref = 'm'
    if b / (10 ** (-0)) > 1:
        valcon2 = round(b / (10 ** (-0)), c + 0)
        pref = ''
    return valcon2, pref



