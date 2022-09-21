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

for name in sorted(linguagens_favoritas.keys()):
    print(f'{name.title()} obrigado por participar da pesquisa.')


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
