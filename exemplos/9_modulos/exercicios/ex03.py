'''Acrescente um atributo chamado number_served cujo valor default é 0.
Crie uma instância chamada restaurant a partir dessa classe. Apresente o
número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e
exiba-o novamente.'''


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        '''Inicializa os atributos'''
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Exibe uma descrição sobre o restaurante'''
        return f'Nome {self.name}. Tipo de culinária {self.type}'

    def open_restaurant(self):
        '''Informa que o restaurante está aberto'''
        return f'{self.name} está aberto'

    def set_number_served(self, customers):
        '''Define o número de clientes atendidos'''
        if customers > 0:
            self.number_served += customers


restaurant = Restaurant('Paraíso', 'mineira')
