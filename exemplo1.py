#def retornar_itens_estoque(setor, *args):
#    print(f'Lista salva no estoque do setor: {setor}:')
#    for item in args:
#            print(item)
#
#retornar_itens_estoque('Administrativo', 'Documentos', 'Livros', 'Pcs')

def lista_de_compras(pessoa, **kwargs):
    fruta = kwargs.get('fruta')
    if fruta is not None:
        print(f'Na lista de compras do {pessoa} há uma fruta: {fruta}')

lista_de_compras('Jureg', fruta='Abacate', massas='macarrão', verdura='couve')
lista_de_compras('Jorel', fruta='Atemoia', sorvete='limao')