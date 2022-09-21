'''Glossário
Pense em três palavras. Use
essas palavras como chaves e armazene seus significados
como valores. Mostra cada palavra e seu significado em uma
saída formatada de modo elegante.'''

glossario = {
    'computador': "maquina destinada ao processamento de dados",
    'internet': "rede de conexões globais",
    'desenvolvedor': "profissional que escreve e cria softwares"
}

for k, v in glossario.items():
    print(f'{k}:\n    {v.title()}')
