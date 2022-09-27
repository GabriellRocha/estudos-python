'''Restaurante: Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e
cuisine_type. Crie um método chamado describe_restaurant() que mostre
essas duas informações, e um método de nome open_restaurant() que exiba
uma mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os
dois atributos individualmente e, em seguida, chame os dois métodos.'''


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        '''Inicializa os atributos restaurant_name e cuisine_type'''
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        '''Exibe uma descrição sobre o restaurante'''
        return f'Nome {self.name}. Tipo de culinária {self.type}'

    def open_restaurant(self):
        '''Informa que o restaurante está aberto'''
        return f'{self.name} está aberto'


restaurant = Restaurant('Paraíso', 'Mineira')
print(restaurant.name)
print(restaurant.type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
