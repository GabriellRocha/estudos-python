def make_pizza(tamanho, *toppings) -> None:
    '''Apresenta a pizza que estamos prestes a preparar'''
    print(f'Fazendo uma pizza tamanho {tamanho} com os seguintes ingredientes')
    for item in toppings:
        print('- ' + item)
