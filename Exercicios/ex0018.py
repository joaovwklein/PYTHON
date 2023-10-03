from math import sqrt
cat1=int(input('Digite o comprimento do primeiro cateto: '))**2
cat2=int(input('Digite o comprimento do segundo cateto: '))**2
hip=sqrt(cat1+cat2) 
print('O valor da hipotenusa do triangulo retangulo e de: {}'.format(hip))
