def scipara5730(a = list()):
    b = a
    local_list = []
    for i, j in enumerate(b):
        #print(i, j)
        comando = str('OUT ' + (f'{j:.7f} ') + 'A')
        local_list.insert(i, comando)
    return(local_list)

def scipara5730b(a):
    b = str(a)
    comando = str('OUT ' + b + 'A')
    return(comando)

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

def prefi2(a, c=1):
    b = a
    if b / (10 ** (-12)) > 1:
        valcon2 = round(b / (10 ** (-12)), c)
        pref = 'p'
    if b / (10 ** (-9)) > 1:
        valcon2 = round(b / (10 ** (-9)), c)
        pref = 'n'
    if b / (10 ** (-6)) > 1:
        valcon2 = round(b / (10 ** (-6)), c)
        #pref = 'μ'
        pref = 'u'
    if b / (10 ** (-3)) > 1:
        valcon2 = round(b / (10 ** (-3)), c)
        pref = 'm'
    if b / (10 ** (-0)) > 1:
        valcon2 = round(b / (10 ** (-0)), c)
        pref = ''
    return valcon2, pref



