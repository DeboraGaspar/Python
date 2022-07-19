entrada = float(input('Uma distância em metros: '))
km = entrada / 1000
hm = entrada / 100
dam = entrada / 10
dm = entrada * 10
cm = entrada * 100
mm = entrada * 1000

print('*** A medida de {}m corresponde a : ***'.format(entrada))
print('-> {}km\n-> {}hm\n-> {}dam\n-> {}dm\n-> {}cm\n-> {}mm '.format(km, hm, dam, dm, cm, mm))
