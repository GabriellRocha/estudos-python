'''Um dicionário em Python é uma coleção de chave-valor.
Cada chave é conectada a um valor, e você pode usar uma
chave para acessar o valor associado a ela.'''

'''Um par chave-valor, é um conjunto de valores assosciados
um ao outro'''

'''O valor de uma chave poder ser um numero, uma string,
uma lista ou até mesmo outro dicionpario. De fato, podemos
usar qualquer objeto que possa ser cirado em Python como
valor de um dicionário'''

pessoa = {'nome': "Gabriel", 'idade': 23}
print(pessoa['nome'])
print(pessoa['idade'])


'''Quando souber que precisará de mais de uma linha para definir um
dicionário maior essa é uma boa prática:'''

linguagens_favoritas = {
    'jen': "Java",
    'sarah': "C",
    'edward': "Ruby",
    'phil': "Python"
}


'''Vamos percorrer o dicionário e quando o nome (chave), for de um dos seus
amigos, exibimos uma mensagem personalizada com sua linguagem favorita'''

amigos = ['phil', 'sarah']

for key in linguagens_favoritas.keys():
    if key in amigos:
        print(f'Oi {key.title()}, sua linguagem favorita é: {linguagens_favoritas[key].title()}')
    else:
        print(f'{key.title()} sua linguagem favorita é: {linguagens_favoritas[key]}')
