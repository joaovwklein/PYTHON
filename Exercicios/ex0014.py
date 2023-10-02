produto=int(input('Informe o preço do produto para poder aplicar o desconto de 5%: '))
porcent=0.05*produto
desc=produto-porcent
print('O valor do produto com o desconto aplicado fica em: {} Reais'.format(desc))