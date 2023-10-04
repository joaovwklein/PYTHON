import random
lista=[0,1,2,3,4,5]
numero_escolhido= random.choice(lista)
num=int(input('Informe um nunmero inteiro entre 0 e 5: '))

if num==numero_escolhido:
    print('Parabéns voce acertou o numero ')

else:
    print('Infelizmente voce errou, mais sorte na proxima')

print('--FIM--')