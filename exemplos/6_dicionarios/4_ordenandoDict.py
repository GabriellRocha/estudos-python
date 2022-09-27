'''Dicionários não são sequencias, logo não mantém nenhuma
ordem específica de seus objetos. Mas é possível exibir os
itens de um dicionário em ordem, usando alguns métodos
interessantes'''

'''Uma maneira de fazer os itens serem devolvidos em determinada
sequencia é ordenar as chaves á medida que são devolvidas no
laço for. Podemos uar a função sorted() para obter uma cópia
ordenada das chaves: '''

linguagens_favoritas = {
    'jen': "Java",
    'sarah': "C",
    'edward': "Ruby",
    'phil': "Python"
}

for chave in sorted(linguagens_favoritas.keys()):
    print(f'{chave.title()} obrigado por participar da pesquisa.')


'''Essa instrução for é como as outras
instruções for, exceto que a função sorted() está em torno do método
dictionary.keys(). Isso diz a Python para listar todas as chaves do
dicionário e ordenar essa lista antes de percorrê-la com um laço.'''


'''Se você estiver mais interessado nos valores contidos em um dicionário,
o método values() pode ser usado para devolver uma lista de valores sem
as chaves.'''

for value in linguagens_favoritas.values():
    print(f'{value.title()}')

'''Essa abordagem extrai todos os valores do dicionário sem verificar se há
repetições. Isso pode funcionar bem com uma quantidade pequena de valores,
mas em uma enquete grande, o resultado seria uma lista com muitas repetições.
'''

'''Outra forma de ordenação de dicionários'''

d = {'b': 3, 'd': 6, 'a': 2, 'c': 7}
ordenada = list(d.keys())
ordenada.sort()
for key in ordenada:
    print(key, '=', d[key])
