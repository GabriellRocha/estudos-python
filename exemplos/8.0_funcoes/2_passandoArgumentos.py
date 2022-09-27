'''Pelo fato de ser possível que uma definição de função
tenha vários parâmetros, uma chamada de função pode precisar
de diversos argumentos.

Argumentos posicionais -> devem estar na mesma ordem em que os
parâmetros foram escritos'''


def describe(animal_type: str, pet_name: str) -> str:
    '''Exibe informações sobre um animal de estimação.'''
    return f'O nome do(a) {animal_type} é {pet_name}'


'''Devemos fornecer o tipo de animal e o nome nessa ordem.'''
print(describe('cachorro', 'pitoco'))


'''Argumentos nomeados -> (keywords arguments) em que cada argumento é
constituído de um nome de variável e de um valor (é um par nome-valor),
ou por meio de listas e dicionários de valores'''


def describee(animal_type: str, pet_name: str) -> str:
    '''Exibe informações sobre um animal de estimação.'''
    return f'O nome do(a) {animal_type} é {pet_name}'


print(describe(animal_type='cachorro', pet_name='pitoco'))

'''Nota: Quando usar argumentos nomeados, lembre-se de usar nomes exatos
dos parâmetros usados na definição da função'''
