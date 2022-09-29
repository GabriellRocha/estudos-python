'''– Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício anterior. Transfira o método show_privileges() para essa classe. Crie
uma instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios.
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


class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        return self.privileges


class Admin(User):
    '''Define um tipo de usuário'''
    def __init__(self, first_name, last_name, age, privilegios):
        super().__init__(first_name, last_name, age)
        self.privileges = privilegios
        '''Instâncias como atributo'''


privileg = Privileges()  # Instância da class Privileges
administrador = Admin('Gabriel', 'Silva', 23, privileg)

print(administrador.privileges.show_privileges())
