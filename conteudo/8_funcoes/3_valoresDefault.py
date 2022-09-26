'''Ao escrever uma função, podemos definir um valor default para cada
parâmetro. Se um argumento para um parâmetro for especificado na
chamada da função, Python usará o valor desse argumento. Se não for,
o valor default do parâmetro será utilizado.'''


def describe(pet_name: str, animal_type='cachorro'):
    '''Exibe informações sobre um animal de estimação.'''
    return f'O nome do {animal_type} é {pet_name}'


'''Agora sempre que chamarmos essa função podemos omitir
a informação animal_type'''

'''Observe que a ordem dos parâmetros na definição da função
precisou ser alterada, pois o único argumento restante na
chamada da função é o nome do animal de estimação. Python
continua interpretando esse valor como argumento posicional,
portanto ele é associado ao primeiro parâmetro da definição da
função.'''

print(describe('pitoco'))

'''Ao usar valores default, qualquer parâmetro com um valor desse
tipo deverá ser listado após todos os parâmetros que não tenham os
valores default. Isso permite que Python possa interpretar os
argumentos posicionais corretamente.'''

