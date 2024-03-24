"""Terceira DAG."""
from time import sleep

from airflow.decorators import dag, task
from datetime import datetime

@dag(dag_id='MinhaPrimeiraDag',description='Primeira DAG',schedule='* * * * *',start_date=datetime(2024,3,24),catchup=False)
def pipeline():
    @task
    def primeira_atividade():
        print('Minha primeira atividade')
        sleep(2)

    @task
    def segunda_atividade():
        print('Minha segunda atividade')
        sleep(2)

    @task
    def terceira_atividade():
        print('Minha terceira atividade')
        sleep(2)

    @task
    def quarta_atividade():
        print('Dag Finalizada')
        sleep(2)


    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4

pipeline()