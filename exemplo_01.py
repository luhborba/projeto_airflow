"""Exemplo 00."""
from time import sleep
from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_atividade():
    logger.info('Minha primeira atividade')
    sleep(2)

def segunda_atividade():
    logger.info('Minha segunda atividade')
    sleep(2)

def terceira_atividade():
    logger.info('Minha terceira atividade')
    sleep(2)

def pipeline():
    while True:
        primeira_atividade()
        segunda_atividade()
        terceira_atividade()
        logger.info('Pipeline concluida')

pipeline()