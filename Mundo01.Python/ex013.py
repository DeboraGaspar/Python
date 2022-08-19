print('$$ REAJUSTE SALARIAL $$')

salario = float(input('Qual o salário do Funcionário?? R$ '))

aumento = salario + (salario * 15 / 100)

print('O salário antigo de R${:.2f}, com reajuste de 15%, passa a ser R${:.2f}!'.format(salario, aumento))