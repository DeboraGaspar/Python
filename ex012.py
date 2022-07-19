print('$$ __Calculando os descontos__ $$')

valor = float(input('~> Informe o valor do produto: R$ '))
desc5 = valor - (valor * 5 / 100)
desc10 = valor - (valor * 10 / 100)
desc15 = valor - (valor * 15 / 100)
desc20 = valor - (valor * 20 / 100)
print('Valor do produto sem desconto: R${:.2f}!!!\n-> Com 5% de desconto: R${:.2f}\n-> Com 10% de desconto: R${:.2f}'
      '\n-> Com 15% de desconto: R${:.2f}'
      '\n-> Com 20% de desconto: R${:.2f}'.format(valor, desc5, desc10,desc15, desc20))
