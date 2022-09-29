'''Nem sempre você precisará começar do zero para escrever uma classe.
Se a classe que você estiver escrevendo for uma versão especializada de
outra classe já criada, a herança poderá ser usada. Quando uma classe
herda de outra, ela assumirá automaticamente todos os atributos e
métodos da primeira classe. A classe original se chama classe-pai e a nova
classe é a classe-filha. A classe-filha herda todos os atributos e método de
sua classe-pai, mas também é livre para definir novos atributos e
métodos próprios.
'''


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


class EletricCar(Car):
    '''Representa aspectos específicos de veículos elétricos.'''
    def __init__(self, marca, modelo, ano):
        '''Inicializa os atributos da classe pai em seguida, inicializa
        os atributos específicos de um carro eletrico'''
        super().__init__(marca, modelo, ano)
        self.batery_size = 70

    #  método específico
    def describe_batery(self):
        '''Exibe uma frase que descreve a capacidade da bateria'''
        return f'Este carro tem uma bateria {self.batery_size} -KWh'


meu_tesla = EletricCar('tesla', 'model S', 2018)
print(meu_tesla.describe_batery())
