'''Preenchendo uma lista com dados de entrada do usuário
em forma de dicionário'''

participantes = []
new_user = {}
active = True

while active:
    new_user['nome'] = input('Digite seu nome: ')
    new_user['idade'] = int(input('Informe sua idade: '))
    participantes.append(new_user.copy())
    resposta = input('Deseja adicionar outro participante? [S/N]').upper()
    if resposta == 'N':
        active = False


respostas = {}
active_2 = True

while active_2:
    nome = input('Digite seu nome: ')
    idade = int(input('Informe sua idade: '))
    '''Lembrete:Essa tecnica será efetiva apenas se os valores das chaves forem
    diferentes, caso tenha duas chaves (nome) identicas uma irá
    sobrepor a outra'''
    respostas[nome] = idade
    repeat = input('Você gostaria de deixar outra pessoa responder? (s/n)')
    if repeat == 'n':
        active_2 = False

print(respostas)
