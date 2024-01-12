medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}M corresponde a \n{}KM \n{}HM \n{}DAM \n{:.1f}DM \n{:.2f}CM \n{:.2f}MM.'.format(medida, km, hm, dam, dm, cm, mm))
