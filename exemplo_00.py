"""Exemplo 00."""
from time import sleep
def primeira_atividade():
    print('Minha primeira atividade')
    sleep(2)

def segunda_atividade():
    print('Minha segunda atividade')
    sleep(2)

def terceira_atividade():
    print('Minha terceira atividade')
    sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print('Pipeline concluida')

pipeline()