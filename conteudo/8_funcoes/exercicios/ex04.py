'''Cidades: Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades
diferentes em que pelo menos uma delas não esteja no país default.'''


def describe_city(name_city: str, country='Brasil') -> str:
    conectivo = 'no'
    if country[-1] == 'a':
        conectivo = 'na'
    return f'Cidade de {name_city} localizada {conectivo} {country}'


cidade_1 = describe_city('São Paulo')
cidade_2 = describe_city('Londres', 'Ingleterra')
cidade_3 = describe_city('Ouro Preto')
print(cidade_1)
print(cidade_2)
print(cidade_3)
