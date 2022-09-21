'''Para acessar um valor associado a uma chave,
especifique o nome do dicionário e coloque a chave
entre colchetes'''


pessoa = {'nome': 'Gabriel', 'idade': 23}
print(pessoa['idade'])

'''Adicionando novos pares de chave-valor'''

pessoa['altura'] = 1.75
print(pessoa)

'''Removendo pares de chave-valor
Podemos usar a instrução del para remover totalmente um par
de chave-valor'''

del pessoa['idade']
print(pessoa)

'''Percorrendo um dicionário com laço for.
Necessário a utilização de duas variavéis auxiliares'''

for k, v in pessoa.items():
    print(f'A chave {k} tem o valor {v} associado.')
