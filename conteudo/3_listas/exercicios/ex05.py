minhas_pizzas = ['calabresa', 'frango', 'bacon', 'mussarela', 'presunto']

friend_pizzas = minhas_pizzas[:]
friend_pizzas.append('peito de peru')

print('Minhas pizzas preferidas são: ')
for pizza in minhas_pizzas:
    print(pizza.title(), end=' ')
