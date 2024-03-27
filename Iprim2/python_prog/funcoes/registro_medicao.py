from datetime import datetime
import conv_num

def data_hora():
    hoje = datetime.now()
    data = hoje.strftime('%d-%m-%Y')
    hora = hoje.strftime('%H:%M:%S')
    return data, hora


def rel(a): # lembrar de colocar temperatura
    with open('registro.txt', 'w+') as file:
        file.write('###### REGISTRO DO ENSAIO ######\n')
        file.write(f'\nRealizado em {data_hora()[0]} com início às {data_hora()[1]} \n')
        file.write(f'\nIDUT[A] / arquivo de leitura                             / VPJVS[V] '
                   f'/ CSU[V]  / Tini[°C] / Tfin[°C] / Uabs [A] / Icalc [A]\n ')
        print(f'\nIDUT[A] / arquivo de leitura      / VPJVS[V] / CSU[nV] / Tini[°C] / Tfin[°C] / Uabs [A] / Icalc [A] ')
        for i in range (0, len(a)):
            for j in range(0, len(a[i])):
                for k in range (0, len(a[i][j])):
                    if k == 2:
                        val = conv_num.prefi2(a[i][j][k], 9)
                        num = val[0]
                        pref = val[1]
                        uni = 'V'
                    if k == 3:
                        val = conv_num.prefi2(a[i][j][k], 2)
                        num = val[0]
                        pref = val[1]
                        uni = 'nV'
                    if k ==4 or k ==5:
                        val = conv_num.prefi2(a[i][j][k], 3)
                        num = val[0]
                        pref = val[1]
                        uni = '°C'

                    if k == 6:
                        #print((a[i][j][k]),type(a[i][j][k]))
                        val = conv_num.prefi2(a[i][j][k], 2)
                        num = val[0]
                        pref = val[1]
                        uni = 'A'
                    if k ==7:
                        #print((a[i][j][k]),type(a[i][j][k]))
                        val = conv_num.prefi2(a[i][j][k], 7)
                        num = val[0]
                        pref = val[1]
                        uni = 'A'
                    if k ==0 or k == 1:
                        num = a[i][j][k]
                        pref = ''
                        uni = ''
                    print(f' {num} {pref}{uni} /', end="")
                    escr = str(f' {num} {pref}{uni} /')
                    print(escr)
                    file.write(f'{escr}')
                    if k == 7:
                        file.write(f'\n')
                    #print(f' {a[i][j][k]} /', end="")
                print('')
            #print(f'\n')



        '''file.write(a +'\n')
        file.write('\nValores de tensão inversa: \n')
        file.write(b +'\n')
        file.write('\nValores de corrente: \n')
        file.write(c + '\n')
        file.write('\nresistencia e incerteza calculada: \n')
        file.write(d + ' +/- ' + e + ' ohm, para k = ' +f)
        file.seek(0,0)'''
        #data_hora2 = data_hora()
        #print(data_hora())
       # print(file.read())
#n = [[['2.0 uA', '4810002_tap2_10_LOG_Wesley.xls', 0.0002000004, 20.6, 5.0, 5.0, 4.0380436877385205e-10, 2.000017458938568e-06], ['26.5 uA', '4810002_tap2_10_LOG_Wesley.xls', 0.0002000004, 20.6, 5.0, 5.0, 4.0380436877385205e-10, 2.000017458938568e-06], ['51.0 uA', '4810002_tap2_10_LOG_Wesley.xls', 0.0002000004, 20.6, 5.0, 5.0, 4.0380436877385205e-10, 2.000017458938568e-06], ['75.5 uA', '4810002_tap2_10_LOG_Wesley.xls', 0.0002000004, 20.6, 5.0, 5.0, 4.0380436877385205e-10, 2.000017458938568e-06], ['100.0 uA', '4810002_tap2_10_LOG_Wesley.xls', 0.0002000004, 20.6, 5.0, 5.0, 4.0380436877385205e-10, 2.000017458938568e-06]]]
#n= [[['2.0 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.00020000039, 20.4, 23.01, 23.023, 3.998943328288558e-10, 2.0000693226460744e-06], ['45.6 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.004560008892, 20.4, 23.01, 23.023, 3.9999771303291205e-10, 4.5601580556330494e-05], ['98.1201 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.0098120291334195, 20.4, 23.01, 23.023, 4.0037348720209536e-10, 9.812350097248253e-05], ['132.5009 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.0132501158376755, 20.4, 23.01, 23.023, 4.0076783644969025e-10, 0.00013250549265649762], ['229.3201 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.0229320547174195, 20.4, 23.01, 23.023, 4.025055061401987e-10, 0.000229328048538065]], [['220.0 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.02200004, 20.4, 23.01, 23.023, 4.0229817568126015e-10, 0.00022000759649011954], ['554.441 uA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.05544421, 20.4, 23.01, 23.023, 4.149263863118751e-10, 0.0005544602364992723], ['1.113 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.11132032, 20.4, 23.01, 23.023, 4.5748450264644225e-10, 0.0011132396142784734], ['1.69 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.16896043, 20.4, 23.01, 23.023, 5.231283629413198e-10, 0.0016896595690842875], ['1.69 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.16900362, 20.4, 23.01, 23.023, 5.231839490153785e-10, 0.0016900914832122804]], [['2.2 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.22000043, 20.4, 23.01, 23.023, 5.939408905620895e-10, 0.002200076264911009], ['6.21 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 0.62101321, 20.4, 23.01, 23.023, 1.302523142069466e-09, 0.006210335241241101], ['12.76 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 1.27600349, 20.4, 23.01, 23.023, 2.5782581398579137e-09, 0.012760452296809655], ['16.3 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 1.63000318, 20.4, 23.01, 23.023, 3.278165601404651e-09, 0.016300564994566], ['21.0 mA', '4810002_tap2_10_LOG_Wesley - Copia.xls', 2.1000041, 20.4, 23.01, 23.023, 4.210893098999154e-09, 0.021000727937785416]]]
#rel(n)