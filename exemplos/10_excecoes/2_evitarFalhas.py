print('Dê-me dois números e eu os dividirei')
print('Informe "q" para sair a qualquer momento')

while True:
    primeiro_numero = input('Primeiro número: ')
    if primeiro_numero == 'q':
        break
    segundo_numero = input('Segundo número: ')
    if segundo_numero == 'q':
        break
    try:
        resposta = int(primeiro_numero) / int(segundo_numero)
    except ZeroDivisionError:
        print('Você não pode dividir por zero.')
    else:
        # Qualquer código que depende do bloco try é adicionado no bloco else
        '''Nesse caso, se a operação for bem-sucedida, usamos o bloco else
        para exibir o resultado'''
        print(resposta)


'''O único código que deve
estar em uma instrução try é aquele que pode fazer uma exceção ser
levantada. Às vezes, você terá um código adicional que deverá ser
executado somente se o bloco try tiver sucesso; esse código deve estar no
bloco else. O bloco except diz a Python o que ele deve fazer, caso uma
determinada exceção ocorra quando ele tentar executar o código que está
na instrução try.
'''
