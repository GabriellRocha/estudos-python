'''Um problema comum ao trabalhar com arquivos é o tratamento de
arquivos ausentes.'''

filename = 'alice.txt'

'''Python não é capaz de ler um arquivo ausente, portanto uma
exceção é levantada'''

try:
    with open(filename) as file_object:
        file_object.read()
except FileNotFoundError:
    message = f'Desculpe, o arquivo {filename} não existe.'
    print(message)

'''O código no bloco try gera um
FileNotFoundError, portanto Python procura um bloco except que trate esse
erro.'''

