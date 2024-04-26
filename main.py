from flask import Flask, url_for, render_template
#modulo render_template serve para buscar na pagina templates os arquivos html e também manda variaveis do back 
#para o front end atraves das variaveis de contexto

#Inicialização
app = Flask(__name__)

#rotas (url_for é ideal para criar urls entre paginas)
@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Rhuan","membro_ativo": True},
        {"nome": "Guilherme","membro_ativo": False},
        {"nome": "Maria","membro_ativo": False}
    ]

    return render_template('index.html',titulo=titulo,usuarios=usuarios)


#rotas
@app.route('/sobre')
def pagina_sobre():
    return 'Não tem nada para vc saber sobre mim'

#Recarrega o servidor o web a cada atualização
app.run(debug=True)
