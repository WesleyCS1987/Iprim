#import banco_dados
import scipy
#import statistics

def constantes(alfa1, beta1, r01, ur01, kr01, t01, ut01, ut1, kt1, rest1):
    alfa = alfa1
    beta = beta1
    r0 = r01
    ur0 = ur01
    kr0 = kr01
    t0 = t01
    ut0 = ut01
    ut = ut1
    kt = kt1
    rest = rest1
    return alfa, beta, r0, ur0, kr0, t0, ut0, ut, kt, rest

def medicao(vpjvs1, csu1, tini1, humini1, tfin1,  humfin1):
    vpjvs = float(vpjvs1)
    csu = float(csu1)
    tini = float(tini1)
    humini = float(humini1)
    tfin = float(tfin1)
    humfin = float(humfin1)
    return vpjvs, csu, tini, tfin

def incerteza(const, medic):
    # Parametros constantes do resistor padrão
    alfa = const[0]
    beta = const[1]
    r0 = const[2]
    uro = const[3]
    kro = const[4]
    t0 = const[5]
    ut0 = const[6]

    # Parametros do termometro
    ut = const[7]
    kt = const[8]
    rest = const[9]

    # Parametros da medição de tensão e da temperatura
    vpjvs = medic[0]
    csu = medic[1]
    tini = medic[2]
    tfin = medic[3]
    tmed = (tini + tfin)/2

    # calculo das constantes k
    k1 = r0 + r0*alfa*t0 + r0*beta*(t0**2) + r0*alfa*tmed + 2*r0*beta*t0*tmed + r0*beta*(tmed**2)
    k2 = vpjvs
    k3 = 1 + alfa*t0 + beta*(t0**2) + alfa*tmed + 2*beta*t0*tmed + beta*(tmed**2)
    k4 = r0 + r0*alfa*t0 + r0*beta*(t0**2)
    k5 = r0*alfa + 2*r0*beta*t0
    k6 = r0*beta
    k7 = r0 + r0*alfa*tmed + r0*beta*(tmed**2)
    k8 = r0*alfa + 2*r0*beta*tmed

    # calculo mensurando
    icalculada = k2/k1

    # calculo dos coeficientes de sensibilidade
    di_dpjvs = 1/k1
    di_dr0 = k2/(k3*(r0**2))
    di_dt = (-k2*k5 - 2*k2*k6*tmed) / ((k4 + k5*tmed + k6*(tmed**2))**2)
    di_dt0 = (-k2*k8 - 2*k2*k6*t0) / ((k7 + k8*t0 + k6*(t0**2))**2)

    # Incerteza padrão
    uvpjvs = csu
    utcert = ut/kt
    utresol = rest/(2*(3**0.5))
    ur0cert = uro/kro
    ut0cert = ut0/(3**0.5)

    # Componentes de incerteza
    comuvpjvs = uvpjvs*di_dpjvs
    comutcert = utcert*di_dt
    comutresol = utresol*di_dt
    comur0cert = ur0cert*di_dr0
    comut0cert = ut0cert*di_dt0

    # Incerteza combinada
    incomb = (comuvpjvs**2 + comutcert**2 + comutresol**2 + comur0cert**2 + comut0cert**2)**0.5

    # Graus de liberdade efetivos
    gl = 1*(10**4)

    # Fator k
    abrang = 0.05 # aqui deverá ser colocado o intervalo de abrangência, neste caso está em 95%
    abrang2 = 1-abrang/2
    fatk = (scipy.stats.t.ppf(abrang2, gl))  #INV.T.BC(0,05;M49) em que M49 são os graus de liberdade efetivos

    # Incerteza expandida
    incexp = incomb*fatk

    return incexp, icalculada



#d = banco_dados.get_res(str('PR07'))
#t = banco_dados.get_termometro()
#const1 = (constantes(d['alfa'], d['beta'], d['r0'], d['ur0'], d['kr0'], d['t0'], d['ut0'], t[0], t[1], t[2]))

#med1 = [1.00000195, 2.04e-8, 23.010, 23.023]

#print(incerteza(const1, med1))