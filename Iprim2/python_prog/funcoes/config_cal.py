import copy

import banco_dados

def sel_res(k):
    a = list()
    res = banco_dados.banco_res()
    calib = banco_dados.banco_calib()
    #print(res)
    #print(calib)
    for i in res:
        #print(i)
        for j in range(0, len(calib[str(k)]["rmax"])):
            #print(res[str(i)]["r0"])
            if (res[i]["r0"]) <= (calib[str(k)]["rmax"][j]["r"]):
                #print(f'para o resistor {res[i]["id"]} faixa sera '
                      #f'{calib[k]["rmax"][j]["range"]}')
                a.append([res[i]["id"], calib[k]["rmax"][j]["range"]])
                #print(a)
    #print(a)
    return a

def faixaspvpjvs(vpjvs, faixas, resistor):
    vpjvsin = vpjvs
    faixasin = faixas
    resistorin = resistor
    faixaspjvs = []

    # Determinar as faixas considerando a tensão minima do VPJVS
    corrminpjvs = vpjvsin / resistorin
    for i in range(0, len(faixasin)):
        if corrminpjvs < faixasin[i]:
            faixaspjvs.append(faixasin[i])
    #print(faixasin)
    #print(faixaspjvs)
    return faixaspjvs


    #print(vpjvsin, faixasin, resistorin)

#d = banco_dados.get_res(str("PT17"))
#r = float(d["r0"])
#faixas1 = [0.00022, 0.0022, 0.01]
#faiteste = faixaspvpjvs(250e-6, faixas1, r)

#sel_res("cal1")

def corrcalib(faixaspcorr, vpjvscorr, resistcorr):
    faixaspcorrin = faixaspcorr
    vpjvscorrin = vpjvscorr
    resistcorrin = resistcorr
    #print(faixaspcorrin, vpjvscorrin, resistcorrin)
    correntesa = []
    correntesb = []
    for i in range(0, len(faixaspcorrin)):
        if i == 0:
            pt1 = (vpjvscorrin / resistcorrin)*10**6
        else:
            pt1 = faixaspcorrin[i-1]*10**6

        if (faixaspcorrin[i] == 0.000219) or (faixaspcorrin[i] == 0.000220):
            pt5 = 219
        elif (faixaspcorrin[i] == 0.00220):
            pt5 = 2100
        elif (faixaspcorrin[i] == 0.0220):
            pt5 = 21000
        elif (faixaspcorrin[i] == 0.220):
            pt5 = 210000
        elif (faixaspcorrin[i] == 2.20):
            pt5 = 2100000
        else:
            pt5 = faixaspcorrin[i]*10**6

        interv = (pt5 - pt1)/4
        for j in range(0, 5):
            correntesa.insert(j, pt1+j*interv)
        ka = copy.deepcopy(correntesa)
        correntesb.insert(i, ka)
        correntesa.clear()
    #print(correntesb)
    return correntesb

#corrcalib(faiteste, 250e-6, r)
def corrcalibabs(cor): # converte a lista de correntes em micro amperes para valores absolutos
    corin = cor
    corabsa = []
    corabsb = []
    for i in range (0, len(corin)):
        for j in range(0, len(corin[i])):
            corabsa.insert(j, corin[i][j]*10**-6)
        kte = copy.deepcopy(corabsa)
        corabsb.insert(i, kte)
        corabsa.clear()
    return corabsb

def corrcalibabsarred(cur):
    curin = cur
    corabsc = []
    corabsd = []
    for i in range(0, len(curin)):
        for j in range(0, len(curin[i])):
            if curin[i][j] < 220e-6:
                curin[i][j] = round(curin[i][j], 10)
            elif curin[i][j] < 2.2e-3:
                curin[i][j] = round(curin[i][j], 9)
            elif curin[i][j] < 22e-3:
                curin[i][j] = round(curin[i][j], 8)
            elif curin[i][j] < 220e-3:
                curin[i][j] = round(curin[i][j], 7)
            elif curin[i][j] < 2200e-3:
                curin[i][j] = round(curin[i][j], 6)
            corabsc.insert(j, curin[i][j])
        kte2 = copy.deepcopy(corabsc)
        corabsd.insert(i, kte2)
        corabsc.clear()
    return corabsd


