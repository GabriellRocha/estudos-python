'''Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se
de incluir um valor de saída no laço while.'''


def make_album(nome_artista: str, titulo_album: str) -> None:
    '''Exibe um dicionário informações sobre um artistae seu álbum
     musical'''
    album = {}
    album["nome"] = nome_artista
    album["titulo"] = titulo_album
    print(album)


while True:
    print('Insira às informações solicitadas')
    nome = input('Nome do artista: ')
    if nome == 'q':
        break
    album = input(f'Informa o título do álbum do(a) {nome}: ')
    if album == 'q':
        break

    make_album(nome_artista=nome, titulo_album=album)
