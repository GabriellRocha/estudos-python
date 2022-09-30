from random import randint

'''Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
Escreva um método chamado roll_die() que exiba um número aleatório entre
1 e o número de lados do dado. Crie um dado de seis dados e lance-o dez
vezes.
Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez
vezes.'''


class Die:
    '''Uma tentativa simples de representar um dado.'''

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        '''Exibe um lado aleatório do dado'''
        return randint(1, self.sides)


print('Emulando o primeiro dado')
dado_1 = Die()
for i in range(1, 11):
    print(f'{i}º Jogada: {dado_1.roll_die()}')

print('\nEmulando o segundo dado')
dado_2 = Die(20)
for i in range(1, 11):
    print(f'{i}º Jogada: {dado_2.roll_die()}')
