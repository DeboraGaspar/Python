entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(entrada))

print('Só tem espaços? ', entrada.isspace())

print('É um número? ', entrada.isnumeric())

print('É alfabético? ', entrada.isalpha())

print('É alfanúmerico? ', entrada.isalnum())

print('Está em maiúsculas? ', entrada.isupper())

print('Está em minúsculas? ', entrada.islower())

print('Está capitalizada? ', entrada.istitle())