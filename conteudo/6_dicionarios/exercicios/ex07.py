'''Crie um dicionário, pense em três nomes para usar como chaves
do dicionário e armazene de um a três lugares favoritos
para cada pessoa'''

dicionario = {
    'Gabriel': ['Minas', 'São Paulo', 'Bahia'],
    'Maria': ['Minas', 'Amazonas'],
    'Luiz': ['Rio do Janeiro']
}

for k, v in dicionario.items():
    print(f'Nome: {k}')
    '''Verificando tamanho da lista para exibir msg personalizada'''
    if len(v) > 1:
        print('Lugares favoritos: ')
        for lugar in v:
            print(lugar, end=' ')
        print()
    else:
        print('Lugar favorito: ')
        print(v[0])
    print('-' * 30)
