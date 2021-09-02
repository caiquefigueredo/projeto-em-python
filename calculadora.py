#Resolvendo de um jeito normal
print('Calculadora! :)')

p1 = input('Você deseja +, -, *, / ou digite s para encerrar: ')
if p1 == '+' or p1 == '-' or p1 == '*' or p1 == '/':
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))

while (p1 != 's'):
    if (p1 == '+'):
        soma = n1 + n2
        print('O resultado: {} + {} = {}'.format(n1, n2, soma))
    elif (p1 == '-'):
        menos = n1 - n2
        print('O resultado: {} - {} = {}'.format(n1, n2, menos))
    elif (p1 == '*'):
        multi = n1 * n2
        print('O resultado: {} * {} = {}'.format(n1, n2, multi))
    elif (p1 == '/'):
        divi = n1 / n2
        print('O resultado: {} / {} = {}'.format(n1, n2, divi))

    else:
        print('Operação Inválida.')

    p1 = input('Você deseja +, -, *, / ou digite s para encerrar: ')
    if p1 == '+' or p1 == '-' or p1 == '*' or p1 == '/':
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))

print('Encerrando o programa...')

