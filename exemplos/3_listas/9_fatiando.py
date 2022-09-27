'''Para criar uma fatia, especifique o índice do primeiro e do último
elemento com os quais você quer trabalhar.'''

jogadores = ['charles', 'martina', 'michael', 'eli', 'pedro', 'florence']
print(jogadores[0:3])

'''Se o primeiro indice de uma fatia for omitido, Python comecará
sua fatia automáticamente no inicio da lista '''
print(jogadores[:4])

'''Uma sintaxe semelhante funcionará se quiser uma fatia que inclua
o final da lista '''
print(jogadores[1:])
