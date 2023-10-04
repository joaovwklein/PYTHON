distancia=int(input('Informe a distancia em Kms da sua viajem: '))

if distancia >= 200 :
    passagem= distancia*0.45
    print('O valor da sua passagem ficou em {} R$' .format(passagem))

else:
    passagem= distancia*0.50
    print('O valor da sua passagem ficou em {} R$' .format(passagem))

print('FIM')    