'''No coração de cada instrução If está uma expressão que pode
ser avaliada como True ou False, chamada teste condicional.
A maioria dos testes condicionais compara o valor armazenado
em uma variável com um valor especifico de interesse'''

carros = ['subaru', 'toyota', 'bmw', 'audi']
for car in carros:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

'''Verificando se um valor está em uma lista'''
frutas = ['banana', 'abacaxi', 'melancia', 'abacate', 'laranja']

print('melancia' in frutas)

'''Verificando se um valor não está em uma lista.'''

usuarios_banidos = ['maria', 'pedro', 'gabriel', 'lucas']
user = 'miguel'
if user not in usuarios_banidos:
    print(user.title())
