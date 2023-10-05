salario=int(input('Informe o seu salario para aplicar o aumento: '))

if salario>=1251:
    taxa=salario*0.10
    aumento=taxa+salario
    print('Voce recebeu {}R$ de aumento, seu salario no final ficou em {}R$'.format(taxa,aumento))

else:
    taxa=salario*0.15
    aumento=taxa+salario
    print('Voce recebeu {}R$ de aumento, seu salario no final ficou em {}R$'.format(taxa,aumento))

print('FIM')