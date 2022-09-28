"""Um conjunto de classes usado para
representar carros à gasolina e elétricos."""


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


class Batery:

    def __init__(self):
        self.batery_size = 70


class EletricCar(Car):
    '''Representa aspectos específicos de veículos elétricos.'''

    def __init__(self, marca, modelo, ano, bateria):
        '''Inicializa os atributos da classe pai em seguida, inicializa
        os atributos específicos de um carro eletrico'''
        super().__init__(marca, modelo, ano)
        self.batery = bateria

    def describe_batery(self):
        '''Exibe uma frase que descreve a capacidade da bateria'''
        return f'Este carro tem uma bateria {self.batery.batery_size} -KWh'


if __name__ == '__main__':
    bateria = Batery()
    carro = EletricCar('tesla', 'A4', 2016, bateria)
    print(carro.describe_batery())
