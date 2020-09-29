x = int(input('Podaj liczbe: '))
if x == 0:
    print('Podaj inna liczbe')
elif x%2 == 0:
    print(str(x) + ' To liczba parzysta')
else:
    print(str(x) + ' To liczba nieparzysta')

