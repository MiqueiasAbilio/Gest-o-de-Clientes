from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_cliente():
    '''listar os clientes'''
    cliente = Cliente.select()
    return render_template('lista_cliente.html', clientes=cliente)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    '''inserir os dados do cliente'''
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )
    return render_template('iten_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    '''formulario para cadatrar clientes'''

    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    '''obter as informações de um cliente'''
    cliente = Cliente.get(Cliente.id == cliente_id)
    return render_template('detalhe_cliente.html',  cliente = cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    '''formulario para editar um cliente'''
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    '''atualizar os dados do cliente'''
    data = request.json
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
    return render_template('iten_cliente.html', cliente = cliente_editado  )

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    '''deletar cliente'''
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_intance()
    return {'dilited': 'ok'}

