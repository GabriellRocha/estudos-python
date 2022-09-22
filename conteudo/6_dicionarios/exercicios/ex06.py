'''Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
'''

pitoco = {
    'tipo': "cachorro",
    'dono': "Gabriel"
}

garfield = {
    'tipo': "gato",
    'dono': "Maria"
}

jabuti = {
    'tipo': "tartaruga",
    'dono': 'João'
}

pets = [pitoco, garfield, jabuti]

for pet in pets:
    print(f'Animal: {pet["tipo"]}. Dono {pet["dono"]}')
