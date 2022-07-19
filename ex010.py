print('~~ Considerando o valor do dólar em US$ 5,41 ~~')
real = float(input('-> Digite quanto você tem na carteira? R$ '))

dolar = real / 5.41

print('>> Com tantos R$ {:.2f}, você pode comprar US$ {:.2f}'.format(real, dolar))