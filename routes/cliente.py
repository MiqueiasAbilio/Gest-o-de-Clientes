from flask import Blueprint, render_template, request
from database.clientes import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_cliente():
    '''listar os clientes'''
    return render_template('lista_cliente.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    '''inserir os dados do cliente'''
    data = request.json
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome":data['nome'],
        "email":data['email']
    }
    CLIENTES.append(novo_usuario)
    return render_template('iten_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    '''formulario para cadatrar clientes'''
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    '''obter as informações de um cliente'''
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    '''formulario para editar um cliente'''
    cliente = None
    for c in CLIENTES:
        if c['id']==cliente_id:
            cliente = c
    return render_template('form_cliente', clente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    '''atualizar os dados do cliente'''
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    '''deletar cliente'''
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]
    return {'dilited': 'ok'}

