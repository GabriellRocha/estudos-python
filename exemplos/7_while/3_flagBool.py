'''Quando temos um programa que muitos eventos diferentes poderiam
faze-lo parar de executar, por exemplo um jogo, podemos definir uma
variável que determina se o programa como um todo deve esta ativo.
Esta variável chamada flag atua como um sinal para o programa'''

active = True
prompt = 'Digite um elogio ou "quit" para encerra: '
while active:
    message = input(prompt)
    if message == 'quit':
        active = False

''' Break
Para sair de um laço while de imediato, sem executar qualquer código
restante no laço, independentemente do resultado de qualquer teste
condicional, utilize a instrução break.'''

''' Continue
Em vez de sair totalmente de um laço sem executar o restante de seu
código, podemos usar a instrução continue para retornar ao início, com
base no resultado de um teste condicional.'''
