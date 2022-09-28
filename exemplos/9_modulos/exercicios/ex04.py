''' Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva
uma classe chamada IceCreamStand que herde da classe Restaurant.
Adicione um atributo chamado flavors que armazene uma lista de sabores de
sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de
IceCreamStand e chame esse método.
'''


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


class IceCreamStand(Restaurant):
    '''Representa aspectos específicos de uma sorveteria'''
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'morango', 'baunilha', 'flocos']

    def flavors_available(self):
        return self.flavors


sorveteria = IceCreamStand('cantinho doce', 'sorveteria')
print(sorveteria.flavors_available())
