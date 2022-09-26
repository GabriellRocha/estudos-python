'''São blocos de código nomeados, concebidos para realizar
uma tarefa específica. Quando queremos executar uma
tarefa em particular, definida em uma função, chamamos
o nome da função responsável por ela. Se precisar
executar essa tarefa várias vezes durante seu programa,
não será necessário digitar todo o código para a mesma
tarefa repetidamente: basta chamar a função dedicada ao
tratamento dessa tarefa e a chamada dirá a Python para
executar o código da função.'''


def greet_user(name: str) -> str:
    '''Exibe uma saudação simples.'''
    return 'Olá, ' + name


print(greet_user('Gabriel'))

'''name -> parâmetro - uma informação de que a função precisa
para executar sua tarefa'''

'''Gabriel em greet_user('Gabriel') argumento - um argumento é
uma informação passada para uma função em sua chamada'''
