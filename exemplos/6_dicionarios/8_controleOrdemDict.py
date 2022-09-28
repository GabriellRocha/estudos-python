from collections import OrderedDict

'''Se você estiver criando um dicionário e quiser manter o controle da
ordem em que os pares chave-valor são adicionados, a classe OrderedDict
do módulo collections poderá ser usada. Instâncias da classe OrderedDict
se comportam quase do mesmo modo que os dicionários, exceto que
mantêm o controle da ordem em que os pares chave-valor são
adicionados.'''

active = True
favorites_linguagens = OrderedDict()
'''Cria um dicionário ordenado vazio e o armazena em favorites_linguagens'''
while active:
    nome = input('Qual o seu nome: ')
    favorites_linguagens[nome] = input(f'{nome} qual sua linguagem favorita? ')
    resp = input('Deseja que mais alguém participe da enquete? (s/n)')
    if resp == 'n':
        active = False

for nome, linguagem in favorites_linguagens.items():
    print(f'{nome.title()} sua linguagem favorita é {linguagem}')

'''Agora o dicionário preserva a ordem em que os itens foram adicionados.'''
