n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

s = n1 + n2

print('o tipo do n1 é:', type(n1), 'e o valor n2 é:', type(n2))

print('A soma de {} mais {} da o valor: {}'.format(n1, n2, s))

A = input('digite algo: ')


print('{} é um numero?'.format(A), A.isnumeric())

print('{} é uma alfa?'.format(A), A.isalpha())

print('{} está com letras maiusculas?'.format(A), A.isupper())

print('{} é um alfa numerico?'.format(A), A.isalnum())
