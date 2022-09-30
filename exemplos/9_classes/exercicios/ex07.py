from collections import OrderedDict

'''Reescreva o programa glossario usando a classe OrderedDict
e certifique-se de que a ordem da saída coincida com a ordem
em que os pares chave-valor foram adicionados ao dicionário.'''

'''Pense em três palavras. Use
essas palavras como chaves e armazene seus significados
como valores. Mostra cada palavra e seu significado em uma
saída formatada de modo elegante.'''


glossario = OrderedDict()

glossario = {
    "computador": 'máquina destinada ao processamento de dados',
    "internet": 'rede de conexões globais',
    "desenvolvedor": 'profissional que escreve e cria softwares'
}

print(glossario)
