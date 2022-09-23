'''Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete.'''


message = 'se pudesse visitar um lugar do mundo, para onde você iria? '
message_2 = 'Deseja que mais alguém responda a essa enquete? (s/n)'
participantes = []
enquete = {}
active = True
while active:
    nome = input('Digite seu nome: ')
    lugar = input(f'{nome}, {message}')
    enquete[nome] = lugar
    repeat = input(message_2)
    if repeat == 'n':
        active = False

print('Resultado')
for k, v in enquete.items():
    print(f'Entrevistado(a) {k}, resposta: {v}')
