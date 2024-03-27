import json
import pandas
import os

'''def cad_res2():
    resistor = {"id": 0, "r0": 0, "uro": 0, "kr0": 0, "t0": 0, "uto": 0, "alfa": 0, "beta": 0}
    for i in resistor:
        if resistor[i] == "x":
            break
        else:
        resistor[i] = input(f'digite {i} ou x para voltar')
        while resistor[i] != "x":
            if'''

def cad_res():
    # carregando o banco de dados de resistores para esta funcao
    #t = input('digite os parametros ou "x" para sair: ')
    with open('res2.json', 'r') as file:
        r_json = file.read()
        r_json = json.loads(r_json)
        #print(r_json)

    resistor = {"id": 0, "r0": 0, "uro": 0, "kr0": 0, "t0": 0, "uto": 0, "alfa": 0, "beta": 0}
    for i in resistor:
        resistor[i] = (input(f'digite {i} '))
        if resistor[i] == "x":
            break
        elif i == "id":
                #resistor[i] = str(input(f'digite {i} '))
                for j, k in r_json.items():
                    #print(print(r_json[str(j)]["id"]))
                    for l in k:
                        while True: # logica para nao digitar resistores com mesma identificacao
                            if l == 'id'and r_json[str(j)][str(l)] == resistor[i]:
                                print("mude o id")
                                resistor[i] = str(input(f'digite {i} '))
                                #continue
                            else:
                                break

        else:
            while resistor[i] != "x":
                try:
                    resistor[i] = float(resistor[i])
                    break
                except:
                    #print("este parametro deve ser um numero real")
                    resistor[i] = input(f"{i} deve ser um numero real. Digite {i}")
                    continue

        if resistor[i] == "x":
            break

    for i in resistor:
        if resistor[i] != "x":
            inc = True
            continue
        else:
            inc = False
            break

    if inc == True:
       # atualizando o valor do banco de dados de resistores
       a = len(r_json)
       r_json[str(a)] = resistor  # atualizando o resistor criado para o banco r_json
       # salvar o novo banco de dados para json e depois carregar em novo arquivo
       r_json = json.dumps(r_json, indent=True)
       with open ('res2.json', 'w+') as file:
            file.write(r_json)

def banco_res():
    with open('resi2.json', 'r') as file:
        resistores = file.read()
        resistores = json.loads(resistores)
        print(resistores[str(0)])
    return resistores

#print(banco_res())
#cad_res()

def cad_calib():
    # carregando o banco de dados de resistores para esta funcao
    with open('cal2.json', 'r') as file:
        c_json = file.read()
        c_json = json.loads(c_json)
        print(c_json)

    calibrador = {"PN": 0, "id": 0, "rmax": [{"range": 0, "r": 0}], "vcomp": 0}
    print('digite os parametros: ')
    for i, m in calibrador.items():
        if i == "id":
            calibrador[i] = str(input(f'digite {i}: '))
            for j, k in c_json.items():
                # print(print(r_json[str(j)]["id"]))
                for l in k:
                    while True:  # logica para nao digitar resistores com mesma identificacao
                        if l == 'id' and c_json[str(j)][str(l)] == calibrador[i]:
                            print(f'já existe id {calibrador[i]}. Colocque um nome ainda não utilizado')
                            calibrador[i] = str(input(f'digite {i}: '))
                        else:
                            break

        elif i == "rmax":
            p = 0
            lista = []
            dici = {}
            resp = 's'
            while resp == 's':
                while True:# bloco que não deixa receber string no lugar de numero
                    r = (input("digite o range"))
                    if r == 'x':
                        break
                    else:
                        try:
                            r = float(r)
                            s = float(input("digite rmax para o range"))
                            dici["faixa"] = r
                            dici["r"] = s
                            lista.append(dici)
                            break
                        except:
                            print("este campo deve ser apenas numero ou 'X'!")
                            continue


                resp = input('há nova faixa? (s/n) ')
                if resp == "s":
                    p = p+1
                    continue
                elif resp == "n":
                    break
                else:
                    while True:
                        resp = input('deve ser apenas s ou n')
                        if resp == "s" or resp =="n":
                            break
                        else:
                            continue

            calibrador[i] = lista

        elif i == 'PN':
            calibrador[i] = str(input(f'digite {i} '))

        else:
            while True:
                try:
                    calibrador[i] = float(input(f'digite {i} '))
                    break
                except:
                    print(f'{i} deve ser numero real \n')
                    continue

    print(calibrador)

    # atualizando o valor do banco de dados de resistores
    a = calibrador["PN"]
    c_json[str(a)] = calibrador  # atualizando o resistor criado para o banco r_json
    print(c_json)

    # salvar o novo banco de dados para json e depois carregar em novo arquivo
    c_json = json.dumps(c_json, indent=True)
    with open('cal2.json', 'w+') as file:
        file.write(c_json)

#cad_calib()

def pegar_med(nome_arq):
    b = nome_arq
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
    csu_pjvs = tabela.iat[linha, coluna4]
    #return linha, coluna, tabela.iat[linha, coluna]
    return data_pjvs, hora_pjvs, vdut_pjvs, csu_pjvs

#ultima_data = loc_cel()



nome = r'C:\Users\Wesley\Desktop\Mestrado INMETRO\Monografia\SAP 3 nova caracterização\resultados_pjvs\4810002_tap2_10_LOG_Wesley.xls'
medicao = pegar_med(nome)
#print(medicao_1[0], medicao_1[1], medicao_1[2], medicao_1[3])
