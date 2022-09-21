'''A função range é uma função nativa da linguagem Python que
é utilizada para gerar uma sequência numérica dentro de um intervalo
determinado. Ela normalmente é utilizada como auxiliar da função for.'''

numeros = list(range(1, 11))
squares = list()
for numero in numeros:
    value = numero ** 2
    squares.append(value)
print(squares)

'''Por padrão o range:
começa em 0
Salto 1
Vai até n-1'''
