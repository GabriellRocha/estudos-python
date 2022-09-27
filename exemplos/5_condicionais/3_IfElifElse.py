'''Muitas vezes, você precisará testas mais de duas situações
possiveis; para avaliar isso, a sintaxe if-elif-else poderá
ser usada. Cada teste condicional e executado em sequencia,
até que um deles passe. Quando um teste passar, o código após
esse teste é executado e ignorará o restante dos teste.
'''

idade = int(input('Informe sua idade: '))
if idade <= 4:
    print('Entrada gratuita :)')
elif idade <= 5 and idade <= 18:
    print('Valor R$ 5.00')
else:
    print('Valor R$ 10.00')

'''O bloco else é uma instrução que captura tudo. Ela corresponde
a qualquer condição não atendida por um teste if ou elif e isso,
às vezes, pode incluir dados inválidos ou até maliciosos.'''

'''Em suma, se quiser que apenas um bloco de cógido seja executado,
utilize uma cadeia if-elif-else. Se mais de um bloco deve ser
executado, utilize uma serie de instruções if independentes.'''
