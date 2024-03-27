import json

#from os import getcwd
import sys
from pathlib import Path


#rpath = Path('res2.json')


def local_path():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS)
    else:
        return Path('.')

base_path = local_path()
#base_path = Path(sys._MEIPASS)

def cad_res():
    # carregando o banco de dados de resistores para esta funcao
    # t = input('digite os parametros ou "x" para sair: ')
    with open(base_path / Path('res2.json'), 'r') as file:
        r_json = file.read()
        r_json = json.loads(r_json)
        # print(r_json)

    resistor = {"id": 0, "r0": 0, "uro": 0, "kr0": 0, "t0": 0, "uto": 0, "alfa": 0, "beta": 0, "imax": 0}
    for i in resistor:
        resistor[i] = (input(f'digite {i} '))
        if resistor[i] == "x":
            break
        elif i == "id":
            # resistor[i] = str(input(f'digite {i} '))
            for j, k in r_json.items():
                # print(print(r_json[str(j)]["id"]))
                for l in k:
                    while True:  # logica para nao digitar resistores com mesma identificacao
                        if l == 'id' and r_json[str(j)][str(l)] == resistor[i]:
                            print("mude o id")
                            resistor[i] = str(input(f'digite {i} '))
                            # continue
                        else:
                            break

        else:
            while resistor[i] != "x":
                try:
                    resistor[i] = float(resistor[i])
                    break
                except:
                    # print("este parametro deve ser um numero real")
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
        with open(base_path / Path('res2.json'), 'w+') as file:
            file.write(r_json)

def banco_res():
    with open(base_path / Path('res2.json'), 'r') as file:
        r_json = file.read()
        r_json = json.loads(r_json)
    return r_json

#print(banco_res())

def get_res(a):
    with open(base_path / Path('res2.json'), 'r') as file:
        r_json = file.read()
        r_json = json.loads(r_json)
        for i in r_json:
            if r_json[str(i)]["id"] == str(a):
                b=i
    return r_json[str(b)]
#print(get_res("PT020"))


'''def cad_calib():
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
                    while True:  # bloco que não deixa receber string no lugar de numero
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
                        p = p + 1
                        continue
                    elif resp == "n":
                        break
                    else:
                        while True:
                            resp = input('deve ser apenas s ou n')
                            if resp == "s" or resp == "n":
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
            file.write(c_json)'''

def banco_calib():
    # carregando o banco de dados de resistores para esta funcao
    with open(base_path / Path('cal2.json'), 'r') as file:
        c_json = file.read()
        c_json = json.loads(c_json)
        #print(c_json)
    return c_json

def get_calib(a):
    with open(base_path / Path('cal2.json'), 'r') as file:
        c_json = file.read()
        c_json = json.loads(c_json)
        for i in c_json:
            if i == str(a):
                b=i
    return c_json[str(b)]
#print(get_calib("cal1"))

#cad_res()

def  cad_termometro():
    pass

def  banco_termometro():
    pass

def get_termometro():
    uterm = 0.005
    kterm = 2
    resterm = 0.001
    return uterm, kterm, resterm


def salv_ens(medi, nome= 'abc'):
    a = medi
    b = (nome + '.json')
    result_json = json.dumps(a, indent=True)
    with open(str(b), 'w+') as file:
        file.write(result_json)
    return result_json

def salv_ens_txt(medi2):
    with open('medicoes_planilha.txt', 'w+') as file:
        file.write(f'{medi2}')
    return medi2

