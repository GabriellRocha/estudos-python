'''Python usa objetos especiais chamados exceções para administrar erros
que surgirem durante a execução de um programa. Sempre que ocorrer
um erro que faça Python não ter certeza do que deve fazer em seguida,
um objeto exceção será criado. Se você escrever um código que trate a
exceção, o programa continuará executando. Se a exceção não for
tratada, o programa será interrompido e um traceback, que inclui uma
informação sobre a exceção levantada, será exibido.'''

'''Dizemos a Python para tentar executar um código e lhe dizemos o que ele deve
fazer caso o código resulte em um tipo particular de exceção.
'''

try:
    print(5/0)
except ZeroDivisionError:
    print('Você não pode dividir por zero.')

'''
Se o código no bloco try causar um erro, o interpretador procurará um bloco
except cujo erro coincida com aquele levantado e executará o código desse
bloco.
'''
