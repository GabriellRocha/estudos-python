'''Se a posição do item quer remover de uma lista
for conhecida, a instrução del pode ser usada'''

frutas = ['banana', 'maça', 'abacaxi']
del frutas[0]

'''O método pop() remove o último item de uma lista,
mas permite que você trabalhe com esse item depois da remoção.'''
popped_frutas = frutas.pop()

'''Também pode utilizar o pop para remover um item de qualquer posição
em uma lista, basta informa o índice'''

popped_fruta = frutas.pop(1)


'''Para remover um item da lista pelo seu valor'''
frutas.remove('maça')
'''Apaga apenas a primeira ocorrência do valor que você especificar'''
