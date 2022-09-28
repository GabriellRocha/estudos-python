'''Uma das primeiras tarefas que você vai querer fazer é
modificar os atributos associados a uma instância em particular.
Podemos modificar os atributos de uma instância diretamente, ou
escrever métodos que atualizem os atributos de formas específicas.'''

'''Todo atributo de uma classe precisa de um valor inicial, mesmo que
esse valor seja 0 ou uma string vazia. Em alguns casos, por exemplo,
quando definimos um valor default, faz sentido especificar esse valor
inicial no corpo do método __init__(), se isso for feito para um
atributo, você não precisará incluir um parâmetro para ele.'''

'''Você pode alterar o valor de um atributo de três maneiras:
podemos modificar o valor diretamente' por meio de uma instância,
definir um valor com um método ou incremeta-lo(somar um determinado
valor a ele).'''


class Car:
    '''Uma tentativa simples de reprsentar um carro'''
    def __init__(self, marca, modelo, ano):
        '''Inicializa os atributos que descrevem um carro'''
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.leitura_odometro = 0

    def get_descriptive_name(self):
        '''Devolve um nome descritivo, formatado de modo elegante.'''
        long_name = f'{self.ano} {self.marca} {self.modelo} milhagem: {self.leitura_odometro}'
        return long_name.title()

    def read_odometer(self):
        '''Exibe uma frase que mostra a milhagem do carro'''
        return f'Este carro tem {self.leitura_odometro} milhas'

    def update_odometer(self, milage: int):
        '''Define o valor de leitura do hodômetro com o valor específicado'''
        if milage >= self.leitura_odometro:
            self.leitura_odometro = milage
        else:
            print('Você não pode reverter um hodômetro!')


meu_carro = Car('audi', 'a4', 2016)
print(meu_carro.get_descriptive_name())
meu_carro.update_odometer(100)
print(meu_carro.get_descriptive_name())
