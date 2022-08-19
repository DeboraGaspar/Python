print('___Conversor de Temperatura___')
temp = float(input('Informe a temperatura em ºC : '))
fahr = (temp * 9/5) + 32
kelvin = temp + 273.15

print('>>> Temperatura Grau Celsius {:.1f} ºC\n>>> Temperatura Grau Fahrenheit {:.1f} ºF\n>>> Temperatura em Kelvin {:.2f} K'.format(temp, fahr,kelvin))