import copy
import time

import banco_dados
import config_cal
import cria_inst
import conv_num
import arqelx_7
import calc_incert
import registro_medicao
import fun_gerais

input('digite enter')

def aps_cadast():
    print("\n ===============\n Resistores cadastrados: ")
    resistores = banco_dados.banco_res()
    print("cad/   id/      r0/    /ur0     /kr0   /t0   /ut0 /alfa   /beta")

    for i in resistores:
        print(f'{i}/  ', end="")
        for j in resistores[str(i)]:
            print(resistores[str(i)][str(j)], end="")
            print("/ ", end="")
        print("")

    print("\n ===============\n Calibradores cadastrados: ")
    print("cad/   PN/      ID/ Vcomp /faixa   /rmax")
    calibradores = banco_dados.banco_calib()
    for i in calibradores:
        print(f'{i}/  ', end="")
        for j in calibradores[str(i)]:
            if j != "rmax":
                print(calibradores[str(i)][str(j)], end="")
                print("/ ", end="")

        for j in calibradores[str(i)]:
            if j == "rmax":
                print("")
                for k in range(0, len(calibradores[str(i)][str(j)])):
                    print("                          ", end="")
                    print((calibradores[str(i)][str(j)][k]['range']), end="")
                    print("/ ", end="")
                    print((calibradores[str(i)][str(j)][k]['r']), end="")
                    print("/ ")
    print("===================================")


def comeco():
    a = int(input('Digite um numero de acordo com a opção:\n'
                  '1 - Iniciar calibração \n'
                  '2 - Cadastrar resistor padrão \n'
                  '3 - cadastrar calibrador \n'
                  '4 - sair do sistema \n'))
    return a

aps_cadast()

if comeco() == 1:

    # conectando o 5730 ao computador
    # =================criar os instrumentos com biblioteca pyvisa=========
    #b = cria_inst.virt_inst()  # criando um intrumento virtual e atribuindo à variavel global b (b=pyvisa.ResourceManager())
    #c = cria_inst.busca_port(b)  # buscar portas disponíveis
    #print(c)

    # ===============conectar o 5730 com a GPIB disponivel===========
    #my_5730 = cria_inst.conecta('GPIB0::6::INSTR', b)  # criando, conectando o instrumento de medição e config write e read termination
    #my_5730.write('STBY')
    #my_5730.write('OUT 0.0000000002 A')
    #my_5730.write('OPER')

    # =====
    b = input("Digite o cad do instrumento que pretende calibrar: ")

    # Para o calibrador escolhido, verificar os resistores que podem ser utilizados para cada faixa do calibrador
    g = banco_dados.get_calib(str(b))  # informacao completa do calibrador guardada em g
    g2 = copy.deepcopy(g['resolucao'])
    # print(len(g2))
    # for iter3 in range (0, len(g2)):
    #    print(g2[iter3]['resoluc'])
    #    print(g2[iter3]['range'])
    # print(g)
    # print(len(g['resolucao']))
    # totresolucao = g.va
    # print(g['resolucao'])
    # print(g['resolucao'][0]['range'])
    c = config_cal.sel_res(str(b))  #
    print("A fonte que será calibrada consegue alimentar os seguintes resistores cadastrados: [id , faixa]")
    for i in c:
        print(i)

    # Usuario selecionar o resistor que ele pretende utilizar
    d = str(input("Digite a id do resistor que irá utilizar: "))
    d = banco_dados.get_res(str(d))  # informacao completa do resistor guardada em d
    h = list()
    for i in c:
        if d["id"] == i[0]:
            h.append(i)  # na lista "h" guardo a escala e o resisotor que sera utilizado na calibracao
    print(f'O resistor {d["id"]} calibra as seguintes faixas do {b} [A]: ', end="")  #
    print('\n')
    for i in h:  # logica para ler cada faixa de corrente para o resistor selecionado
        print(f'{i[1]}/ ', end="")
    print('\n')
    # print(h)

    # carregando as constantes do resistor e termometro para o programa principal
    t = banco_dados.get_termometro()
    const1 = (calc_incert.constantes(d['alfa'], d['beta'], d['r0'], d['ur0'], d['kr0'], d['t0'], d['ut0'], t[0], t[1],
                                     t[2]))
    # print(const1)

    # recebendo e verificando corrente máxima que vai ser gerada no resistor
    imax = float(d['imax'])  # variavel será usada no ajuste fino do PJVS
    while True:
        f = float(input(
            f'Digite a corrente máxima em amperes em que você vai submeter o resistor {d["id"]}  \n'
            f'(ATENÇÃO, O MÁXIMO RECOMENDADO' f'PELO FABRICANTE do {d["id"]} É DE {d["imax"]} A: '))

        if f <= float(d["imax"]):
            break
        else:
            print(f"!!! NÃO DANIFIQUE O {d['id']}, digite uma corrente de no máximo {d['imax']} !!!")
    print('\n')

    # Determinando as faixas que podem ser calibradas a partir:
    # UNO - Da corrente digitada acima (corrente máxima)
    # DOIS - Da corrente que vai gerar a tensão de 250µV (corrente minima definida pela minima leitura do PJVS)
    faixas1 = list()
    faixa2 = list()
    comp_fai = list()
    for i in h:
        if i[1] <= f:
            faixas1.append(i[1])
            comp_fai.append(i[1])
        elif i[1] > f:  # obtendo a última faixa a ser calibrada para a corrente maxima escolhida
            max_fai = i[1]
            faixa2.append(f)

    try:
        faixa2.append(min(faixa2))
        set_faixa2 = set(faixa2)  # eliminando os itens duplicados
        faixa2 = list(set_faixa2)
    except:
        faixa2 = None

    if faixa2 is not None:
        faixas1.extend(faixa2)
    faixas1.sort()

    if faixa2 is None:
        print(f'Esta corrente máxima possibilitará que faixas {comp_fai} seja(m) calibrada(s) totalmete. \n')
    else:
        print(f'Esta corrente máxima possibilitará que faixas {comp_fai} seja(m) calibrada(s) totalmete e a\n'
              f' faixa {max_fai} seja calibrado até {faixas1[-1]} A')

    # Definindo 5 pontos para cada faixa (mesmo a incompleta)
    print(faixas1)
    valor_resistor = float(d["r0"])
    faixas1 = config_cal.faixaspvpjvs(250e-6, faixas1, valor_resistor)
    correntes2 = config_cal.corrcalib(faixas1, 250e-6, valor_resistor)
    correntes4 = config_cal.corrcalibabs(correntes2)
    correntes1 = config_cal.corrcalibabsarred(correntes4)

    print(f'faixas1 = {faixas1}')
    print(f'correntes2 = {correntes2}')
    print(f'correntes4 = {correntes4}')
    print(f'correntes1 = {correntes1}')
    '''correntes1 = []
    corr = []
    min = round((250e-6) / (float(d["r0"])), 12)
    print(faixas1, min)
    primeirafaixa = True
    for i in range(0, len(faixas1)):
        if faixas1[i] > min:
            if primeirafaixa == False:
                pt1 = ptoproximafaixa

            if primeirafaixa == True:
                pt1 = min
                if faixas1[i] == 0.00022:
                    pt5 = 219
                    ptoproximafaixa = 220
                if faixas1[i] == 0.002200:
                    pt5 = 2100
                    ptoproximafaixa = 2200
                if faixas1[i] == 0.022:
                    pt5 = 21000
                    ptoproximafaixa = 22000
                if faixas1[i] == 0.22:
                    pt5 = 210000
                    ptoproximafaixa = 220000
                if faixas1[i] == 2.2:
                    pt5 = 2100000
                    ptoproximafaixa = 2200000
                primeirafaixa = False
                pt5 = float(faixas1[i]*10^6)
            interv = (faixas1[i] - min) / 5
            if i == (len(faixas1) - 1):
                interv = (faixas1[i] - min) / 4
            # correntes1.clear()
            for j in range(0, 5):
                corr.insert(j, min + j * interv)
            k = copy.deepcopy(corr)
            correntes1.insert(i, k)
            corr.clear()
        # correntes2.append(correntes1)
        min = faixas1[i]
        # print(correntes1)
    # print(correntes1)
    # print(faixas1)'''

    # apresenta faixas e valores de corrente sem usar nano, micro e mili
    for i in range(0, len(faixas1)):
        corre = []
        fai = conv_num.prefi2(faixas1[i])
        for j in range(0, len(correntes1[i])):
            corre2 = conv_num.prefi2(correntes1[i][j])
            corre.insert(j, corre2)
            # print(f'Na faixa de {fai} A, valores de corrente [A]: {corre}')
        # print(f'Na faixa de {faixas1[i]} A, valores de corrente [A]: {correntes1[i]}')
        corforn = str(f'{corre[j][0]} {corre[j][1]}A')
        faifor = str(f'{fai[0]} {fai[1]}A')
        print('Na faixa de', faifor, ' valores de corrente: ', end="")
        for k in range(0, len(corre)):
            correfor = str(f'{corre[k][0]} {corre[k][1]}A; ')
            print(correfor, end="")
        print('')
    print(correntes1)

    # converter listas para apresentar em nano, micro e mili // deletar este bloco e testar sem ele
    # prefixoscorrentes = list()
    # for i in range(0, len(faixas1)):
    # prefixoscorrentes.insert(i, conv_num.prefi(correntes1[i]))
    # print(prefixos)
    # print(prefixoscorrentes)

    # converter a lista para valores interpretaveis pelo 5730
    valor_conv = list()
    for i in range(0, len(faixas1)):
        # print(i)
        valor_conv.insert(i, conv_num.scipara5730(correntes1[i]))
    # print(valor_conv)
    # print(correntes1)

    # Comandar e medir o 5730
    interv = int(input('Digite o período de cada ensaio [s]'))
    interv2 = int(input('Digite o tempo de estabilização [s]'))
    list_medicao_corr1 = []
    list_medicao_corr2 = []
    list_medicao_corr3 = []
    list_pjvs1 = []
    list_pjvs2 = []
    corrforn = []  # lista que vai armazenar as correntes efetivamente fornecidas para o resistor padrão
    corrforconv = []
    '''temp1 = input('Para o ajuste do TAP do PJVS, digite a temperatura do laboratório [°C]:')
    #valor_resisistor = d['r0']
    valor_resistor = round(fun_gerais.rpadagora(d, temp1),7)# resistor com 7 casas decimais
    print(f'Valor do resistor para {temp1}  °C é de {valor_resistor:.7f} Ω')'''
    endereco = input('Prepare o PJVS para a leitura, digite o endereço da pasta e pressione enter:')
    for i in range(0, len(correntes1)):
        print(correntes1[i])

        # pegar a resolucao da faixa (cadastrar resolucao do calibrador em ordem crescente)
        for iter3 in range((len(g2) - 1), -1, -1):
            resolu3 = (g2[iter3]['resoluc'])
            faixx = (g2[iter3]['range'])

            if faixx >= correntes1[i][-1]:
                resolu2 = resolu3
                resolu2micro = resolu2 / (10 ** -6)
                faixx2 = faixx
        print(f'resolução desta faixa de {faixx2} é de {resolu2} A ({resolu2micro} μA) ')
        casasresolu = len(str(resolu2micro)) - 2

        for j in range(0, len(correntes1[i])):
            #endereco = input('Prepare o PJVS para a leitura, digite o endereço da pasta e pressione enter:')
            print(j)
            temp1 = input('Para o ajuste do TAP do PJVS, digite a temperatura do laboratório [°C]:')
            # valor_resisistor = d['r0']
            valor_resistor = round(fun_gerais.rpadagora(d, temp1), 7)  # resistor com 7 casas decimais
            print(f'Valor do resistor para {temp1}  °C é de {valor_resistor:.7f} Ω')
            time.sleep(3)
            correntes3 = correntes1[i][j]  # em correntes3 será armazenado o valor de corrente ajustada para o PJVS
            correajus = correntes3
            tap = float(correntes3 * valor_resistor)
            print(tap, type(tap))
            enter2 = input(f'Prepare o PJVS para o TAP de {tap:.9f} V, pressione ESPAÇO e depois ENTER.'
                           f'(Após este enter o calibrador vai gerar a corrente de {correntes3}) A')
            escrev5730 = conv_num.scipara5730b(correntes3)
            print(escrev5730)
            #my_5730.write(valor_conv[i][j])
            #my_5730.write(escrev5730)
            #my_5730.write('OPER')
            print(f'Gerando a corrente {correntes3} A por {interv2} s no resistor de {valor_resistor} Ω.')
            time.sleep(interv2)
            resp = input(f'No resistor de {valor_resistor} Ω há a tensão de {tap:.9f} V. Esta tensão'
                         f' permitiu "tap" para o PJVS (s/n)?')
            while (resp == 'n'):
                #my_5730.write('STBY')
                print(f'\nintervalos em torno da corrente alvo calculada [A]:'
                      f'\n10% - {correntes3 * 0.9} / {correntes3} / {correntes3 * 1.1}'
                      f'\n20% - {correntes3 * 0.8} / {correntes3} / {correntes3 * 1.2}'
                      f'\n30% - {correntes3 * 0.7} / {correntes3} / {correntes3 * 1.3}')
                correajusmicro = float(input(f'Digite uma nova corrente em μA dentro dos intervalos acima.'
                                             f'Respeite a resolução de {resolu2micro} μA:'))
                correajus = correajusmicro * (10 ** -6)
                print(f'corrente de ajuste {correajusmicro} μA ({correajus} A)')

                while correajus > imax:
                    correajusmicro = float(input((f'{correajusmicro} μA maior que a máxima corrente permitida para o'
                                                  f' resistor {d["id"]}, (de {imax} A). Digite uma corrente máxima de {imax}.'
                                                  f'Respeite a resolução de {resolu2micro} μA:')))
                    correajus = float(correajusmicro * (10 ** -6))
                novatensao = correajus * valor_resistor
                print(f'Para o TAP de {tap:.9f} V será gerada corrente de {correajus} A '
                               f'e sobre o resistor padrão de {valor_resistor} Ω haverá nova tensão de '
                               f'{novatensao:.9f} V')
                #enter3 = input(f'Para o TAP de {tap:.9f} V será gerada corrente de {correajus} A '
                               #f'e sobre o resistor padrão de {valor_resistor} Ω haverá nova tensão de '
                               #f'{novatensao:.9f} V. Pressione ESPAÇO depois ENTER ')
                escrev5730 = conv_num.scipara5730b(correajus)
                #my_5730.write(escrev5730)
                print(escrev5730)
                #my_5730.write('OPER')
                resp = input(f'a tensão de {novatensao:.9f} V permitiu "tap" para o PJVS (s/n)? ')
            # else:
            # corrforn.insert(j, correajus) # lista que guarda as correntes fornecidas ao RPAD
            # corrforconv.insert(j, conv_num.prefi2(correajus, casasresolu))  # lista que guarda as correntes fornecidas convertidas em mili, micro, nano
            # print('estabilização finalizada')
            # print('Estabilização finalizada')
            print('estabilização finalizada')
            print(f'j = {j} / tipo do j = {type(j)} / correajus = {correajus} / tipo correajus = {type(correajus)}')
            corrforn.insert(j, correajus)  # lista que guarda as correntes fornecidas ao RPAD
            corrforconv.insert(j, conv_num.prefi2(correajus, 3))
            for num_med in range(0, 1):  # laço para o caso de haver 5 medições
                tempfaixa = float(input('Digite a temperatura do laboratorio para o inicio da medição [ºC]'))
                humi = input('Digite a humidade do laboratorio para o inicio da medição [%]')
                print(f'Gerada a corrente {correajus} para a medição {num_med}')
                for tempo in range(0, interv):
                    print(f'{tempo} s restantes')
                    time.sleep(1)
                print('Finalizado o período para medição')
                tempfaixa2 = float(input('Digite a temperatura do laboratorio no final da medição [ºC]'))
                humi2 = input('Digite a humidade do laboratorio no final da medição [%]')
                enter = input('Pressione "ESPAÇO" depois "ENTER" após o PJVS gerar o excel')
                #my_5730.write('STBY')
                planilha = arqelx_7.serie_medidas2(endereco, tempfaixa, humi, tempfaixa2, humi2)
                print(planilha)

                # bloco que calcula a incerteza logo após a medição
                csu = float(planilha[0][4]) * 10 ** -9
                medicoes = [planilha[0][3], csu, planilha[0][5], planilha[0][7]]
                # print(medicoes)
                medicoeseincert = calc_incert.incerteza(const1, medicoes)
                print(medicoeseincert)
                # dados_consolid = [planilha, medicoeseincert]

                # corforn = str(f'{corre[j][0]} {corre[j][1]}A')
                corrfornec = str(f'{corrforconv[j][0]} {corrforconv[j][1]}A')
                print(f'correntes fornecidas: {corrfornec}')
                dados_consolid = [corrfornec, planilha[0][0], planilha[0][3], planilha[0][4], planilha[0][5],
                                  planilha[0][7],
                                  medicoeseincert[0], medicoeseincert[1]]

                # salvando os valores medidos em uma lista
                # list_pjvs1.insert(j, copy.deepcopy(planilha))
                list_pjvs1.insert(j, copy.deepcopy(dados_consolid))
                time.sleep(interv)
                # medi_corr = my_5730.query('OUT?')
                # medi_corr = num_med*100
                # list_medicao_corr1.insert(num_med, copy.deepcopy(medi_corr))
                # list_medicao_corr1.insert(num_med, medi_corr)
                # time.sleep(interv2)

            # tempfaixa = float(input('digite a temperatura do laboratorio [ºC]'))
            # time.sleep(3)
            # my_5730.write('OPER')
            # for num_med2 in range(0,5):
            # planilha = arqelx_7.loc_cel('Vdu', '4810002_tap2_10_LOG_Wesley.xls')
            # endereco = input('digite o endereco da pasta')
            # enter = input('pressione enter após o PJVS gerar o excel')
            # planilha = arqelx_7.serie_medidas2(endereco, tempfaixa)
            # list_pjvs1.insert(j, copy.deepcopy(planilha))
            # my_5730.write('STBY')
            # list_medicao_corr2.insert(j, copy.deepcopy(list_medicao_corr1))
            # my_5730.write('STBY')
            list_medicao_corr1.clear()
        # list_medicao_corr3.insert(i, copy.deepcopy(list_medicao_corr2))
        list_pjvs2.insert(i, copy.deepcopy(list_pjvs1))
        list_pjvs1.clear()
    # print(list_medicao_corr3)
    # print(list_medicao_corr3)
    # cria_inst.fonte(valor_conv[i], interv)
    # my_5730.write('OUT 0.0000002A')
    # my_5730.write('OUT 2uA') # microamperes é u, miliamperes é m.
    # my_5730.write('OUT 1mA')

    # banco_dados.salv_ens(list_medicao_corr3, 'dafonte')
    print(list_pjvs2)
    # print(list_pjvs2[0])
    # print(list_pjvs2[0][0])
    # print(list_pjvs2[0][0][0])
    # my_5730.write('RST') # ainda nao testei este comando 14set23
    # banco_dados.salv_ens(list_pjvs2, 'dopjvs2')
    # print(banco_dados.salv_ens_txt(list_pjvs2))
    registro_medicao.rel(list_pjvs2)

    # buscar no arquivo os valores lidos pelo PJVS
    # print(arqelx_7.loc_cel('Vdu', '4810002_tap2_10_LOG_Wesley.xls'), type(
    # arqelx_7.loc_cel('Vdu', '4810002_tap2_10_LOG_Wesley.xls')))  # o retorno de arqlelx é uma tupla com duas posições
    # sendo a [0] a linha e a [1] a coluna

    # calc_incert(d)
