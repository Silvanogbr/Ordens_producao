#BACK-END FLASK: Rotas da API rest

from flask import Flask, jsonify, request
from flask_cors import CORS
from database import init_bd, get_connection

#Cria uma instancia da aplicação Flash
app = Flask(__name__, static_folder='static', static_url_path='')

#habilitar os CORS
CORS(app)

#ROTA N1 - Pagina incial
@app.route('/') 
def index():
    #ALIMENTAR ARQUIVO INDEX.HTML DA PASTA STATIC
    return app.send_static_file('index.html')

#ROTA N2 - Status API
@app.route('/status')
def status():
    """Rota de verificação da API(SAÚDE)
    Retornar um JSON informando qual o servidor esta ativo"""
    return jsonify({
        "status": "online",
        "sistema": "Sistema de ordem de produção",
        "versao": "1.0.0",
        "mensagem": "olá, fábrica, API FUNCIONANDO!"
    })

#ROTA N3 - Listar todas as ordens(get)
@app.route('/ordens', methods=['GET'])
def listar_ordens():
    """
    LISTAR TODAS AS ORDENS DA PRODUÇÃO CADASTRADAS.
    MÉTODOS HTTP: GET
    URL: http://localhost/ordens
    Retorna: Lista e ordens em formato JSON
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT *FROM ordens ORDER BY id DESC')
    ordens = cursor.fetchall()
    conn.close()    
    
    #Converte cada Row do SQLite em dicionario para serializar em JSON
    return jsonify([dict(o) for o in ordens])

#PONTO DE PARTIDA

if __name__=='__main__':
    init_bd()
    
    app.run(debug=True, host='0.0.0.0', port=5000)