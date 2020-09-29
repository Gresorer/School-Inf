import math
# x = int(input('Podaj liczbe: '))
# if x == 0:
#     print('Podaj inna liczbe')
# elif x%2 == 0:
#     print(str(x) + ' To liczba parzysta')
# else:
#     print(str(x) + ' To liczba nieparzysta')

# a = int(input('Podaj liczbe: '))
# if a%3==0:
#     print('Liczba jest podzielna przez 3')
# elif a%5==0:
#     print('Liczba jest podzielna przez 5')
# elif a%3==0 and a%5==0:
#     print('Liczba jest podzielna przez 3 i 5')
# else:
#     print('Podzielna przez to i to')
def ZAD4():
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    def CheckB():
        if b==0:
            print('Nieskonczenie wiele rozwiazan')
        else: 
            print('rownanie sprzeczne')
    if a==0:
        CheckB()
    else:
        x = -(b/a)
        print(x)    


def ZAD5():
    year = int(input('Podaj rok: '))
    if year%4==0 and not year%100==0 or year%400==0:
        print('Jest przestepny')
    else:
        print('Nie jest przestepny')


def ZAD6():
    c = int(input('Podaj liczbe c: '))
    if c<23:
        print(c, 23, 56)
    elif c>56:
        print(23, 56, c)
    else:
        print(23, c, 56)

def ZAD7():
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    c = int(input('Podaj liczbe c: '))

    if a==0:
        print('To nie jest rownanie kwadratowe')
        exit()
    else:
        delta = math.sqrt(b)-(4*a*c)
        if delta<0:
            print('Rownanie kwadratowe nie ma perwiastkow rzeczywistych')
            exit()
        else:
            if delta==0:
                x1 = -b/2*a
                x2 = x1
            else:
                x1 = (-b-math.sqrt(delta))/2*a
                x2 = (-b+math.sqrt(delta))/2*a
            print(x1,x2)

#https://teams.microsoft.com/_#/pdf/viewer/teams/https:~2F~2Fliceumkozy.sharepoint.com~2Fsites~2FRozszerzenie~2FShared%20Documents~2FGeneral~2F9%20p%C4%99tle%20-%20while...pdf?threadId=19:103b364ff1004eeaa204600170f99f7f@thread.tacv2&baseUrl=https:~2F~2Fliceumkozy.sharepoint.com~2Fsites~2FRozszerzenie&fileId=1a4e3067-77c1-4048-abea-6a54a705f160&ctx=files&rootContext=items_view&viewerAction=view