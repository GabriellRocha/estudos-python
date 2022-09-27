'''O método sort altera a ordem da lista de forma
permanente. Os carros agora estão em ordem alfabética e não podemos
mais retornar à ordem original.'''

lista_carros = ['bmw', 'audi', 'subaru', 'toyota']
lista_carros.sort()

'''Também podemos ordenar essa lista em ordem alfabética inversa,
passando o argumento reverse=True ao método sort'''

lista_carros.sort(reverse=True)
'''A ordem da lista foi permanentemente alterada'''


'''Para preservar a ordem original de uma lista, mas apresentá-la de forma
ordenada, podemos usar a função sorted()'''

lista_frutas = ['maça', 'abacaxi', 'banana', 'uva', 'melancia']
print(sorted(lista_frutas))

'''Observe que reverse() não reorganiza em ordem alfabética inversa; ele
simplesmente inverte a ordem da lista'''

lista_frutas.reverse()
print(lista_frutas)
