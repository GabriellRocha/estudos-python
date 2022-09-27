'''Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez.
'''


def sanduiche(*itens):
    '''Exibe a lista de ingredientes pedidos.'''
    print('Preparando sanduíche com os sguintes ingredientes: ')
    for item in itens:
        print('- ' + item.title())


sanduiche('hamburguer', 'queijo')
sanduiche('hamburguer', 'queijo', 'bacon', 'alface')
sanduiche('hamburguer', 'gorgonzola', 'rucula', 'maionese')
