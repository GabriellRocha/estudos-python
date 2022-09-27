'''você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.'''

convidados = ['Fátima', 'Pedro', 'José', 'Rebeca']
print('O convidado(a) José não poderá comparecer')

''' Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.'''
desistiu = convidados.index('José')

convidados[desistiu] = 'Lucas'

'''Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.'''

for convidado in convidados:
    print(f'{convidado}, gostaria de vir jantar em casa hoje a noite? ')

'''Adicone novos convidados em posições especificas na lista'''
convidados.insert(0, 'Matheus')
convidados.insert(3, 'Larissa')

'''Remova os conviados da sua lista um de cada vez, exibindo uma mensagem
do porque não poderá convida-la mais. Deixa apenas dois convidados'''

length = len(convidados)
while length > 2:
    removido = convidados.pop()
    print(f'Desculpe {removido}, infelizmente não posso convidá-lo!')
    length -= 1
print(convidados)

'''Utilize del para remover os dois últimos nomes de sua lista, de modo que
você tenha uma lista vazia.'''
del convidados[-1]
del convidados[-1]
print(convidados)
