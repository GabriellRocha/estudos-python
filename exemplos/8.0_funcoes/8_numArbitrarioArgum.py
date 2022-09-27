'''Às vezes você não saberá com atecedência quantos
argumentos uma função deve aceitar.Felizmente, Python
permite que uma função receba um número arbitrário
de argumentos da instrução de chamada
Por exemplo, considere uma função que prepare uma pizza. Ela deve
aceitar vários ingredientes, mas não é possível saber com antecedência
quantos ingredientes uma pessoa vai querer..
'''


def make_pizza(*toppings):
    '''Exibe a lista de ingredientes pedidos.'''
    print('Fazer uma pizza com os seguintes recheios: ')
    for top in toppings:
        print('- ' + top.title())


'''Essa sintaxe funciona, não importa quantos argumentos a função receba'''
make_pizza('calabresa', 'queijo', 'cebola', 'azeitona')

'''O asterisco no nome do parâmetro *toppings diz a Python para
criar uma tupla vazia chamada toppings e reunir todos os
valores recebidos nessa Tupla.'''
