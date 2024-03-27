#Este programa localiza a celula do excel que começa com 'zz'
# assim, se a célula nunca se repetir, basta obter o conteudo dela pela função .iat.
# caso seja necessário localizar a célula, basta utilizar esta funcao a partir das letras inicias
# do  conteudo desejado ou de uma celula adjacente a ele.

import pandas
import os

def loc_cel(conteudo, nome_arq):
    a = conteudo
    #b = nome_arq
    b = nome_arq
    print(a, type(a), b, type(b))
    tabela = pandas.read_excel(b)
    #print(tabela.iat[0,0])
    #print(tabela)
    #print('================================')
    #print(tabela.itertuples())
    for i in tabela.itertuples():
        k = int(i[0])
        l = len(i)-1
        #print(type(l))
        #print(i)
        #print(i[1])
        #print(type(i))
        #print(len(i))
        for n in range(0,l):
            #print(tabela.iat[k,n])
            p = str(tabela.iat[k, n])
            if p.startswith(a):
                #print(p)
                #print(f'{p} encontra-se na linha indice {k}, coluna {n}')
                linha = k
                coluna = n
    coluna= coluna +0
    linha = linha +7
    print(tabela.iat[linha, coluna])
    return linha, coluna, tabela.iat[linha, coluna]

#print(loc_cel('Vdut', '4810002_tap2_10_LOG_Wesley.xls'))

def loc_plan(endereco): # funcao que recebe um endereço e retorna uma lista com 'data' o nome do aquivo mais recente
    caminho = endereco  #no diretorio endereco
    #caminho = r'C:\Users\Wesley\Desktop\Mestrado INMETRO\Monografia\SAP 3 nova caracterização\resultados_pjvs' # se
    # endereço recebido de input não é necessário iniciar com r'...
    #print(caminho)
    arquivos = os.listdir(caminho)
    #print(arquivos)

    lista_datas = []
    for i in arquivos: # em i está cada arquivo dentro de arquivos
        data = os.path.getmtime(f'{caminho}/{i}') # em data é armazenada a data em segundos do salvamento do arquivo
        lista_datas.append((data, i)) # armazenar em uma lista tuplas que combinam cada arquvo(nome) com a data

    lista_datas.sort(reverse=True)#ordenando a lista de datas em ordem decrescente(o ultimo arquivo é o de"data"maior)
    #ultimo_arq = lista_datas[0][0]
    #print(ultimo_arq)
    #print(lista_datas)
    arq_mais_recente = lista_datas[0]
    return arq_mais_recente

def lista_arqu(endereco2): #obtém a lista de arquivos dentro do diretorio endereco2
    caminho2 = endereco2
    arquivos2 = os.listdir(caminho2)
    return arquivos2

def pegar_med(end_absoluto, nome_do_arquivo, tempfai, humi, tempfai2, humi2):
    tempfa = tempfai
    hum = humi
    tempfa2 = tempfai2
    hum2 = humi2
    nome_do_ark = nome_do_arquivo
    b = end_absoluto
    tabela = pandas.read_excel(b)
    #print(tabela.iat[0,0])
    #print(tabela)
    #print('================================')
    #print(tabela.itertuples())
    for i in tabela.itertuples():
        k = int(i[0])
        l = len(i)-1
        for n in range(0,l):
            #print(tabela.iat[k,n])
            p = str(tabela.iat[k, n])
            if p.startswith('Vdut'):
                linha = k # a linha que identifica 'Vdut', 'Date', 'Time' e 'CSU' é a mesma, por isso não é guardada nos
                coluna = n # outros if abaixo
            if p.startswith('Date'):
                coluna2 = n
            if p.startswith('Time'):
                coluna3 = n
            if p.startswith('CSU'):
                coluna4 = n
    #coluna= coluna +0
    #linha = linha +7
    print(coluna, coluna2, coluna3, coluna4)
    linha = tabela.index.max() # sempre vai pegar a última linha da tabela (linha é index)
    #print(tabela.index.max())
    #print(tabela.iat[linha, coluna])
    data_pjvs = tabela.iat[linha, coluna2]
    hora_pjvs = tabela.iat[linha, coluna3]
    vdut_pjvs = tabela.iat[linha, coluna]
    vdut_pjvs = float(vdut_pjvs) # linha que permite ler valores decimais do excel com '.' ao invés de ','
    #print(type(vdut_pjvs))
    csu_pjvs = tabela.iat[linha, coluna4]
    csu_pjvs = float(csu_pjvs) # linha que permite ler valores decimais do excel com '.' ao invés de ','
    #return linha, coluna, tabela.iat[linha, coluna]
    return nome_do_ark, data_pjvs, hora_pjvs, vdut_pjvs, csu_pjvs, tempfa, hum, tempfa2, hum2

#b = input('digite o endereco da pasta')

def serie_medidas(end):
    b = end
    i = int(0)
    med_PJVS = []
    ultimo = loc_plan(b)[0]
    d = loc_plan(b) #d[0] é a 'data mais recente' e d[1] é o nome o arquivo com esta data ############# (03/JUN)  trazer lista dos nomes dos arquivos de loc_plan
    print(d)
    arq_atual = f'{b}/{d[1]}'
    nome_arq = f'{d[1]}'
    medicao = pegar_med(arq_atual, nome_arq)
    med_PJVS.insert(i, medicao)
    print(med_PJVS, med_PJVS[i][0], med_PJVS[i][1], med_PJVS[i][2], med_PJVS[i][3])#med_PJVS[i][0] é o nome do arquivo que
    #t = b #estou medindo; med_PJVS[i][1], med_PJVS[i][2], med_PJVS[i][3] e med_PJVS[i][4] demais resultados da planilha
    #print(t, type(t))
    while True:
        inc = True
        c = input('há nova medição? (s/n)')
        if c == 's':
            d = loc_plan(b)  # d[0] é a 'data mais recente' e d[1] é o nome o arquivo com esta data
            arq_atual = f'{b}/{d[1]}'
            nome_arq = f'{d[1]}'
            medicao = pegar_med(arq_atual, nome_arq)
            lista_arquivos = lista_arqu(b)
            for percorrer_medicoes in lista_arquivos:
                if percorrer_medicoes == medicao[0]:
                    for perc_PJVS in med_PJVS:
                        if perc_PJVS[0] == medicao[0]:
                            #print(perc_PJVS, perc_PJVS[0])
                            if medicao[1] == perc_PJVS[1] and medicao[2] == perc_PJVS[2]:
                                print(f'No arquivo mais recente, {medicao[0]}, NÃO HÁ NOVA MEDIÇÃO')
                                inc = False
            if inc == True:
                i = i + 1
                med_PJVS.insert(i, medicao)
                print(f'Incluida nova medição da planilha {medicao[0]}, data {medicao[1]}, hora {medicao[2]}')
                        # for percorrer_med_PJVS in med_PJVS:# ====(03/JUN)percorrer a pasta de arquivos ao inves de med_PJVS====
                        # if percorrer_med_PJVS == percorrer_medicoes: # situacao em que med_PJVS está no mesmo arquivo

                #ultimo = a
                '''print(f'HÁ NOVA MEDIÇÃO, ÚLTIMO ARQUIVO: {d}')
                print(d[1], type(d[1]))
                arq_atual = f'{b}/{d[1]}'
                print(arq_atual, type(arq_atual))
                data_atu = pegar_med(arq_atual)
                #print(med_PJVS[i][0], med_PJVS[i][1], data_atu[0], data_atu[1])
                #if med_PJVS[i][1][0] != data_atu[0] or med_PJVS[i][1][1] != data_atu[1]:
                if med_PJVS[i][1][0] != data_atu[0] or med_PJVS[i][1][1] != data_atu[1]:
                    i = i+1
                    nome_valores = [arq_atual, pegar_med(arq_atual)]
                    print(nome_valores)
                    med_PJVS.insert(i, nome_valores)
                    #med_PJVS.insert(i, pegar_med(arq_atual))
                else:
                    print('embora com nova data e hora, o arquivo nao apresenta nova leitura')
                print(med_PJVS)'''
            continue
        else:
            break
    return med_PJVS

def serie_medidas2(end, tfaixa=23, hu=50, tfaixa2=23, hu2=50):
    tfaix = tfaixa
    hum = hu
    tfaix2 = tfaixa2
    hum2 = hu2
    b = end
    i = int(0)
    med_PJVS = []
    ultimo = loc_plan(b)[0]
    d = loc_plan(b) #d[0] é a 'data mais recente' e d[1] é o nome o arquivo com esta data ############# (03/JUN)  trazer lista dos nomes dos arquivos de loc_plan
    #print(d)
    arq_atual = f'{b}/{d[1]}'
    nome_arq = f'{d[1]}'
    medicao = pegar_med(arq_atual, nome_arq, tfaix, hum, tfaix2, hum2)
    med_PJVS.insert(i, medicao)
    #print(med_PJVS, med_PJVS[i][0], med_PJVS[i][1], med_PJVS[i][2], med_PJVS[i][3])#med_PJVS[i][0] é o nome do arquivo que
    #t = b #estou medindo; med_PJVS[i][1], med_PJVS[i][2], med_PJVS[i][3] e med_PJVS[i][4] demais resultados da planilha
    #print(t, type(t))
    inc = True
    d = loc_plan(b)  # d[0] é a 'data mais recente' e d[1] é o nome o arquivo com esta data
    arq_atual = f'{b}/{d[1]}'
    nome_arq = f'{d[1]}'
    medicao = pegar_med(arq_atual, nome_arq, tfaix, hum, tfaix2, hum2)
    lista_arquivos = lista_arqu(b)
    #for percorrer_medicoes in lista_arquivos:
        #if percorrer_medicoes == medicao[0]:
            #for perc_PJVS in med_PJVS:
                #if perc_PJVS[0] == medicao[0]:
                    #print(perc_PJVS, perc_PJVS[0])
                    #if medicao[1] == perc_PJVS[1] and medicao[2] == perc_PJVS[2]:
                        #print(f'No arquivo mais recente, {medicao[0]}, NÃO HÁ NOVA MEDIÇÃO')
                        #inc = False
    #if inc == True:
        #i = i + 1
        #med_PJVS.insert(i, medicao)
        #print(f'Incluida nova medição da planilha {medicao[0]}, data {medicao[1]}, hora {medicao[2]}')
                        # for percorrer_med_PJVS in med_PJVS:# ====(03/JUN)percorrer a pasta de arquivos ao inves de med_PJVS====
                        # if percorrer_med_PJVS == percorrer_medicoes: # situacao em que med_PJVS está no mesmo arquivo
    #print(med_PJVS)
    return med_PJVS

#print(serie_medidas(b))
