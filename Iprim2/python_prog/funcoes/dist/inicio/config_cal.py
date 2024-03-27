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

#sel_res("cal1")


