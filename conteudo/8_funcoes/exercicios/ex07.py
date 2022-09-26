'''Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista'''

magicos = ['Houdini', 'Manchu', 'Jasper', 'David']


def show_magicians(magicos: list) -> None:
    '''Exibe os nomes de uma lista de mágicos'''
    for magic in magicos:
        print(magic)


'''modifique a lista de mágicos acrescentando a expressão o Grande ao nome
de cada mágico. Chame show_magicians() para ver se a lista foi
realmente modificada.
'''


def make_great(magicos: list) -> None:
    '''Exibe os nomes de magicos de modo elegante.'''
    for i in range(len(magicos)):
        magicos[i] = 'O Grande ' + magicos[i]
    show_magicians(magicos)


'''Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.'''

copia_magicos = make_great(magicos[:])  # Devolve uma cópia da lista
show_magicians(magicos)  # Lista original
