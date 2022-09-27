'''Sem pastrami: Usando a lista sandwich_orders, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches.
'''
sandwich_orders = [
    'x-bacon', 'pastrami', 'x-tudo', 'pastrami', 'x-frango', 'pastrami']

finished_sandwich = []

mensagem = 'Desculpem clientes, mas estamos sem o pastrami hoje :('
print(mensagem)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami':
        finished_sandwich.append(sandwich)

print('Sanduíches prontos!')
print('-' * 20)
for sandwich in finished_sandwich:
    print(sandwich)
