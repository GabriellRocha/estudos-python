'''Na programação orientada a objetos, escrevemos classes
que representam entidades e situações do mundo real, e criamos
objetos com base nessas classes. Quando escrevemos uma classe,
definimos o comportamento geral que toda uma
categoria de objetos pode ter'''

'''Pense em uma classe como um conjunto de instruções para criar uma
instância.'''


class Dog:
    '''Uma tentavia simples de modelar um cachorro.'''

    def __init__(self, nome, idade):
        '''Inicializa os atributos nome e idade'''
        self.nome = nome
        self.idade = idade

    def sit(self):
        ''''simula um cachorro sentando em resposta a um comando..'''
        return self.nome.title() + ' agora esta sentado'

    def roll_over(self):
        ''''simula um cachorro rolando em resposta a um comando..'''
        return self.nome.title() + ' rolou!'


'''O método __init__() é um método especial em Python executa
automaticamente sempre que criamos uma nova intância baseada
na classe Dog. Esse método não tem uma instrução return explícita,
mas Python devolve automaticamente uma instância que representa
esse cachorro.'''

'''O parâmtro self é obrigatório na definição do método e deve estar antes
dos demais parâmetros. Deve estar incluido na definição pois, quando Python
chama esse método depois(para criar uma instância de Dog), a chamada do método
passará o argumento self automaticamente.

self, é uma referência à própria instância, de modo automático;
ele dá acesso aos atributos e métodos da classe à instância
individual.

As duas variáveis definidas tem o prefixo self, significa que usa o valor
armazenado no parâmetro 'nome' e o armazena na variável 'nome', que é então
associada a uma instância criada. O mesmo vale para idade.
Variáveis como essas, acessíveis por meio de instâncias
são chamadas de atributo.
'''

meu_dog = Dog('pitoco', 4)
print(meu_dog.roll_over())
print(meu_dog.sit())
