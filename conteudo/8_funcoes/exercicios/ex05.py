'''– Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum.'''


def make_album(name_artista: str, titulo_album: str, faixas='') -> dict:
    '''Exibe um dicionário com informações sobre uma artista e seu álbum
    musical'''
    album = {}
    if faixas:
        album["nome"] = name_artista
        album["titulo"] = titulo_album
        album["faixas"] = int(faixas)
        return album
    else:
        album["nome"] = name_artista
        album["titulo"] = titulo_album
        return album


artista = make_album(name_artista='Gustavo Lima', titulo_album='O embaixador')
print(artista)
artitas_1 = make_album(name_artista='Gustavo Lima',
                       titulo_album='O embaixador', faixas='13')
print(artitas_1)
