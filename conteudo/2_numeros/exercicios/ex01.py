''' Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.'''

print('Calculadora de múltiplo')
print('-' * 25)
numero = int(input('Informe um número: '))
if 10 % numero == 0:
    print(f'{numero} é múltiplo de dez')
else:
    print(f'{numero} não é múltiplo de dez')
