'''Até agora trabalhamos com apenas uma informação do
usuário de cada vez. Recebemos a entrada do usuário e
então a exibimos ou apresentamos uma resposta a ela.
Contudo, para controlar muitos usuários e informções,
precisaremos utilizar listas e dicionarios com nossos
laços while.
Um laço for é eficiente para percorrer uma lista, mas você não deve
modificar uma lista em um laço for, pois Python terá problemas para
manter o controle dos itens da lista. Para modificar uma lista enquanto
trabalha com ela utilize um laço while'''

#  Transferindo itens de uma lista para outra

usuarios_nao_confirmados = ['Gabriel', 'José', 'Pedro', 'Lucas']
usuarios_confirmados = []

'''Python interpreta uma lista não vazia como True.'''
while usuarios_nao_confirmados:  # Executa enquanto a lista não estiver vazia
    # Remove e retorna o último item da lista
    usuario_atual = usuarios_nao_confirmados.pop()
    print(f'Verificando usuário {usuario_atual}')
    usuarios_confirmados.append(usuario_atual)

for user in usuarios_confirmados:
    print(f'{user.title()} ok!')


#  Removendo todas as intâncias de valores específicos de uma lista

fruits = ['banana', 'maça', 'banana', 'melancia', 'laranja', 'banana']

while 'banana' in fruits:
    fruits.remove('banana')  # Remove a primeira ocorrência do valor

print(fruits)
