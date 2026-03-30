#Criação e configuração do banco de dados SQLite
import sqlite3

#Constatnte coom o nome do arquivo de banco de dados
#O arquivo será criado durante a primeira execução
bd_ordem = 'ordens.bd'

def get_connection():
    '''
    Cria e retorna uma coneção com o banco de dados SQLite
    
    a propriedade row_factory permite acessar as colunas pelo nome
    (ex: ordem['produto'] em vez de pelo indice(ex: ordem[1]))
    
    retorna:
        sqlite3.connection: objeto de conexão com o banco de dados.
    '''

    conn = sqlite3.connect(bd_ordem)
    conn.row_factory = sqlite3.Row
    return conn

def init_bd():
    '''
    iniciliza o banco de dados criando a tabela 'ordens' se ela ainda nn existir. Seguro para chamar
    multiplas vezes.
    '''
    conn = get_connection()
    
    #cursor() permitir executar comandos SQL
    cursor = conn.cursor()
    
    #if not exist garante que o comando nao falhe se a tabela ja existir 
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS ordens(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       produto      TEXT        NOT NULL,
                       quantidade   INTEGER     NOT NULL,
                       status       TEXT        DEFAULT 'pendente',
                       criado_em    TEXT        DEFAULT(datetime('now', 'localtime'))
                       )
                       ''')
    
    #commit() salvar as alterações no arquivo .bd
    conn.commit()
    
    #close() liberar a conexão
    conn.close()
    
    print("Banco de Dados Inicializado com Sucesso")

