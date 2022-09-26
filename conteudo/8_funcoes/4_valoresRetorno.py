'''Um função nem sempre precisa exibir sua saida diretamente.
Em vez disso, ela pode processar alguns dados e então devolver
algum valor ou um conjunto de valores. O valor devolvido pela
função é chamado valor de retorno. Valores de retorno permitem
passar boa parte do trabalho pesado de um programa para funções
o que pode simplicar o corpo do seu programa.'''


def get_formated_name(primeiro_nome: str, segundo_nome: str) -> str:
    '''Devolve um nome completo formatado de forma elegante.'''
    full_name = primeiro_nome + ' ' + segundo_nome
    return full_name.title()


'''Quando chamamos uma função que devolve um valor, precisamos fornecer
uma variável que o valor de retorno possa ser armazenado.'''

nome = get_formated_name('gabriel', 'silva')
print(nome)


'''Deixando um argumento opcional'''


def geet_formated_name(primeiro_nome: str, ultimo_nome: str, nome_meio='') -> str:
    '''Devolve um nome completo formatado de forma elegante'''
    if nome_meio:
        '''Python interpreta strings não vazias como True'''
        full_name = primeiro_nome + ' ' + nome_meio + ' ' + ultimo_nome
    else:
        full_name = primeiro_nome + ' ' + ultimo_nome
    return full_name.title()


nome_1 = geet_formated_name(primeiro_nome='gabriel',
                            nome_meio='rocha', ultimo_nome='silva')
nome_2 = geet_formated_name('gabriel', 'silva')
print(nome_1)
print(nome_2)
