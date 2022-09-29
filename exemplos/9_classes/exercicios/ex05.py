'''Admin: Um administrador é um tipo especial de usuário. Escreva uma
classe chamada Admin que herde da classe User.Adicione um atributo
privileges que armazene uma lista de strings como "can add post", "can
delete post" "can ban user", e assim por diante. Escreva um método chamado
show_privileges() que liste o conjunto de privilégios de um administrador. Crie
uma instância de Admin e chame seu método.
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


class Admin(User):
    '''Define um tipo de usuário'''
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        '''Exibe os previlégios desse tipo de usuário.'''
        return self.privileges


administrador = Admin('Gabriel', 'Silva', 23)
print(administrador.show_privileges())
