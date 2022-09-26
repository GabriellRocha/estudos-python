'''Vamos usar a função greet_user() com o laço while,
para saudar os usuários de modo mais formal.'''


def greet_user(primeiro_nome: str, segundo_nome: str) -> str:
    '''Exibe uma saudação simples.'''
    full_name = primeiro_nome + ' ' + segundo_nome
    print('Olá, ' + full_name.title())


while True:
    print("Porfavor me diga seu nome!")
    print("Digite 'q' em qualquer momento para sair.")
    primeiro_nome = input('Digite seu primeiro nome:\n')
    if primeiro_nome == 'q':
        break
    segundo_nome = input('Digite seu nome do meio:\n')
    if segundo_nome == 'q':
        break

    greet_user(primeiro_nome, segundo_nome)
