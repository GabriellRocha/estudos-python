'''O for toma uma coleção de itens e executa um
bloco de código uma vez para cada item da coleção.
Em comparaçao, o laço while executa durante o tempo
em que, ou enquanto, uma determinada condição
for verdadeira'''

cont = 1
while cont <= 3:  # while for true
    print(cont)
    cont += 1

'''Outro exemplo'''

prompt = 'Digite uma mensagem ou "quit" para encerrar o programa: '
message = ''
while message != 'quit':
    message = input(prompt)
