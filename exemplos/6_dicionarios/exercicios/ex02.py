'''Use um dicionário para armazenar os números favoritos
de algumas pessoas.'''

numeros_favoritos = {
    'gabriel': 4,
    'lucas': 6,
    'pedro': 7,
    'joao': 8,
    'matheus': 2
}

for k, v in numeros_favoritos.items():
    print(f'O número favorito do {k} é: {v}')
