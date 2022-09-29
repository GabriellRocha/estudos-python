'''Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada
ao usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário.
'''


class User:

    def __init__(self, first_name, last_name, age):
        '''Inicializa os atributos de um usuário'''
        self.nome = first_name
        self.sobrenome = last_name
        self.idade = age
        self.login_attempts = 0

    def describe_user(self):
        '''Apresenta um resumo personalizado das informações do usuário'''
        return f'Nome completo: {self.nome} {self.sobrenome}. Idade {self.idade}'

    def greet_user(self):
        '''Saudação personalizada'''
        return f'Oi, me chamo {self.nome}. Tenha um ótimo dia!'

    def increment_login_attempts(self):
        '''Incrementa o valor de login_attempts em um'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Reinicia o valor de login_attempts com zero'''
        self.login_attempts = 0


pessoa_1 = User('Gabriel', 'Silva', 23)
