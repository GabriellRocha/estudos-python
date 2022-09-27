'''Aninhamento de dicionários'''

r = {
    'nome': {'primeiro_nome': "Gabriel", 'ultimo_nome': "Silva"},
    'conhecimentos': ['Python', 'Html'],
    'idade': 23
}

'''
r -> Dicionário
nome -> Chave que tem como valor um dicionário
primeiro_nome -> chave, "Gabriel" -> Valor
ultimo_nome -> chave, "Silva" -> valor
conhecimentos -> chave, que tem como valor uma lista
idade -> chave, 23 -> valor
'''
print(r['nome'])  # Retorna nome completo
print(r['nome']['primeiro_nome'])  # Retorna o primeiro nome
print(r['conhecimentos'])  # Retorna uma lista
r['conhecimentos'].append('Java')  # Insere um item na lista
print(r['conhecimentos'][-1])  # Retorna o último item da lista
