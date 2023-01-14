n1 = int(input('digite um numero: '))

n2 = int(input('digite um segundo numero: '))

n3 = bool(input('tem um valor dentro de n3?'))

s = n1 + n2
n = float(n1)
b = float(n2)
print('o n1 é tipo',type(n),'e o n3 é tipo ', type(b)) # mentira :)

print('tem um valor dentro de n3? {}'.format(n3))

# print('A soma de', n1, 'mais', n2, 'vai resultar em: ', s) formato antigo do python

print('a soma entre {} e {} vale {}'.format(n1, n2, s))
