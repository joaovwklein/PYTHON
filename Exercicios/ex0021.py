velocidade=int(input('Informe a velocidade do carro: '))
multa=(velocidade-80)*7
if velocidade >=81 :
    print('Voce foi multado, deverá pagar 7,00 R$ por Km ultrapassado, ou seja sua multa final ficou em {} R$.'.format(multa))

else:
    print('Voce não ultrapassou o limite de velocidade, continue assim')

print('FIM')