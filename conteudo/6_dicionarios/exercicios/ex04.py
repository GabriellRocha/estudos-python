'''Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser '''


rios_importantes = {
    'nilo': "egito",
    'amazonas': "brasil",
    'congo': "africa"
}


for rio, pais in rios_importantes.items():
    print(f'O {rio} corre pelo(a) {pais}')

print('Rios salvos no dicionário:')
for rio in rios_importantes.keys():
    print(rio.title())

print('Países salvo no dicionário: ')
for pais in rios_importantes.values():
    print(pais.title())
