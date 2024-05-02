from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente',__name__)

#Listar os clientes
@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html',clientes=CLIENTES)

#Inserir os dados do cliente
@cliente_route.route('/',methods=['POST'])
def inserir_cliente():
    data = request.json
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email']
    }

    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html',cliente=novo_usuario)

#Formulario para cadastrar um cliente
@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

#Exibir detalhes do cliente
@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')


#Formulario para editar um cliente
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')

#Formulario para atualizar  um cliente
@cliente_route.route('/<int:cliente_id>/update',methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass

#Formulario para deletar  um cliente
@cliente_route.route('/<int:cliente_id>/delete',methods=['DELETE'])
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
    return {'deleted': 'ok'}