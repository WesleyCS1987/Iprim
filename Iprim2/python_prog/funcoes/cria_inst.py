import pyvisa
#import time


def virt_inst(): # criar instrumento virtual
    a = pyvisa.ResourceManager()
    return a


def busca_port(a1): # buscar postas disponíveis
    a2 = a1.list_resources()
    return a2


def conecta(endereco, instrumento): # conectar endereço na porta
    d = instrumento.open_resource(endereco)
    d.read_termination = '\n'  # Sem esta linha ao executar read() é buscada toda INFO disponivel do bufer
    d.write_termination = '\n'
    # identificar o ID 3458
    #print(instrumento.query('ID?'))
    return d

'''def fonte(lista, tempo):
    b = lista
    print(b, tempo)
    for i in b:
        
    return'''

'''def escala(instr,valor):
    instr.write(valor)'''