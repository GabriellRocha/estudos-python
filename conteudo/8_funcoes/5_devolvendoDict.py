'''Uma função pode devolver qualquer tipo de valor necessário, incluindo
estruturas de dados mais complexas como listas e dicionários. '''


def construir_pessoa(primeiro_nome: str, segundo_nome: str,
                     idade: int, profissao='') -> str:
    '''-> Devolve um dicionário com informações sobre uma pessoa
    -> Parâmetro profissao é opcional.'''
    person = {}
    if profissao:
        person["nome"] = primeiro_nome
        person["segundo_nome"] = segundo_nome
        person["idade"] = idade
        person["profissao"] = profissao
    else:
        person["nome"] = primeiro_nome
        person["segundo_nome"] = segundo_nome
        person["idade"] = idade
    return person


pessoa = construir_pessoa('Gabriel', 'Rocha', 23)
pessoa_2 = construir_pessoa('Gabriel', 'Rocha', 23, 'Garçom')
print(pessoa)
print(pessoa_2)
