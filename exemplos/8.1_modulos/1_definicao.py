import pizza
'''Quando python lê a esse arquivo, a linha 1 lhe diz para abrir
o arquivo pizza.py e copiar todas as funções dele para esse
programa'''

'''Um módulo é um arquivo terminado em .py que contém o código que
queremos importar para o nosso programa'''

'''Forneça o nome do módulo seguido do nome da função, separados
por um ponto'''

pizza.make_pizza('M', 'Frango', 'Mussarela', 'Catupiry')


'''Podemos importar também uma função específica de um módulo. Eis a
sintaxe geral para essa abordagem:

from nome_do_modulo import função_1, função_2

Quando importamos explicitamente a função podemos chamá-la(s) pelo nome'''

'''Podemos dizer a Python para importar todas as funções de um módulo
usando o operador asterisco (*).
Como todas as funções são importadas, podemos chamar qualquer função pelo
nome, sem usar a notação de ponto. No entanto, é melhor não usar essa
abordagem quando trabalhar com módulos maiores, que não foram escritos
por você: se o módulo tiver um nome de função que seja igual a um nome
existente em seu projeto, você poderá ter alguns resultados inesperados.
Python poderá ver várias funções ou variáveis com o mesmo nome e, em vez
de importar todas as funções separadamente, ele as sobrescreverá.
'''
