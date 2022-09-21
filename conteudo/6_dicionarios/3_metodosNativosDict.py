pessoa = {'nome': "Gabriel", 'idade': 23, 'altura': 1.75, 'casado': False}

'''Esse método retorna todas as chaves de um dicionário em uma lista'''
print(pessoa.keys())


'''Retorna todos os valores de um dicionário em uma lista'''
print(pessoa.values())


'''Retorna uma lista de tuplas de todos os valores e chaves relacionadas'''
print(pessoa.items())


'''Pega o conteúdo de cada chave'''
print(pessoa.get('idade'))


'''Remove a chave especificada e retorna o valor correspondente'''
item = pessoa.pop('altura')
print(item)


'''Usado para descobri o tamanho de uma coleção do tipo dicionário'''
print(len(pessoa))


'''Copia os elementos de um dicionário para inserir em outro'''
outra_pessoa = pessoa.copy()
print(outra_pessoa)


'''Remove todos os elementos do dicionário'''
pessoa.clear()
print(pessoa)
