# faça um programa que leia o seu sucessor e antecessor



#val1 = int(input('coloque o numero para ver seu sucessor e antecessor: '))

#print('o seu valor é: {}'.format(val1), end=' || ')

#val1 = val1 + 1

#print('o seu succesor é: {}'.format(val1), end=' || ')

#val1 = val1 - 2

#print('o seu antecessor é: {}'.format(val1))
#

# faça um programa que leia o seu sucessor e antecessor

Val = int(input('digite um valor para ver o sucessor e o antecessor'))

ant = Val - 1
suc = Val + 1

print('o numero escolhido foi: '.format(Val), end=' |||| ')
print('o seu sucessor é {} e seu antecessor é {} '.format(suc, ant))

# crie um algoritimo que leia um numero e mostre sua dobra

n1 = int(input('digite um valor e veja a sua dobra:  '))

d = n1 * 2 # dobrar o valor

T = n1 * 3 # o triplo do numero

raiz = n1**(1/2) # raiz quadrada

print('o numero escolhido é {} n/ o dobro de {} é {} n/ O triplo é {} n/ e a raiz de {} é {}'.format(n1,n1,d,T,n1,raiz))
