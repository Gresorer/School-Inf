PRINT_INTRO = '############################## PRINT ##############################'
print(PRINT_INTRO, '\n')

print('Hello')    # just print
print(20*'-')    # print '-' text 20 times
print('\n \t')    # \n move to next line, \t add space
print('Hello', 'World', sep=' add text between variables ')
for num in range(5):
    print(num, end=', ')    # after all arguments will be printed whats in end=' '
print('\n0, 1, 2, 3, 4, 5, 6, 7\n')

VARIABLES_INTRO = '############################## VARIABLES ##############################'
print(VARIABLES_INTRO, '\n')

def VARIABLES():    # function isn't needed but it will scope variables
    a = 20    # int type variable, just number
    b = 2.4    # float type variable, number after dot
    c = 'Text'   # string type variable, text
    d = True    # bool type variable, true or false
    e, f = 'First', 2    # you can write variable in that way
    g = h = 'Same'    # in that way you assign all of given variables same value
    i = 'Nice'
    i = 'Python is' + i    # add variable when other action
    j = a + b    # you can add variable to variables
    k = 20
    k += 20    # that means the same as k = k + 20
    print('a:', a,'b:',b,'c:',c,'d:',d,'e:',e,'f:',f,'g:',g,'h:',h,'i:',i,'j:',j,'k:',k,'\n',sep='  ')
VARIABLES()

DATATYPE_INTRO = '############################## DATA TYPE ##############################'
print(DATATYPE_INTRO, '\n')

def DATA():
    a = 'Hello'    # type string
    b = 20    # type int
    c = 20.5    # type float
    d = 2j    # type complex
    e = ['first', 'second', 'third']    # type list
    f = ('first', 'second', 'third')    # type tuple
    g = range(5)    # type range, from 0 to specific number
    h = {'name': 'Andre', 'age': 20}    # type dict
    i = {'ice', 'vvs'}    # type set
    j = frozenset({'ice', 'vvs'})    # type frozenset
    k = True    # type bool
    l = b'hello'    # type bytes
    m = bytearray(5)    # type bytearray
    n = memoryview(bytes(5))    # type memoryview

    # type(a,b)    # in that way you can check a type of variable

    a = str(a)    # change to string type by str()
    b = int(b)    # change to int type by int()
    c = float(c)    # change to float type by float()

    print('  a:', a,'b:',b,'c:',c,'d:',d,'\n','e:',e,'f:',f,'g:',g,'h:',h,'\n','i:',i,'j:',j,'k:',k,'l:',l,'\n','m:',m,'n:',n,'\n',sep='  ')
DATA()

STRINGS_INTRO = '############################## STRINGS ##############################'
print(STRINGS_INTRO, '\n')

def STRINGS():
    a = 'Hello World'
    print('  a: ',   a[1]   ,end='  ')    # it'll print character in position 1 in this ex. it will be 'e'
    b = 'Hello World'
    print('b: ',   b[1:5]   ,end='  ')    # it'll print characters from position 1 to 5 
    c = 'Hello World'
    print('c: ',   len(c)   ,end='  ')    # lenght of variable
    d = 'Hello World'
    print('d: ',   d.strip()   ,'\n',end='  ')    # remove white space from beginning or end
    e = 'Hello World'
    print('e: ',   e.lower()   ,end='  ')    # string will be in lower case
    f = 'Hello World'
    print('f: ',   f.upper()   ,end='  ')    # string will be in upper case
    g = 'Hello World'
    print('g: ',   g.capitalize()   ,end='  ')    # string will be in capitalize
    h = 'Hello World'
    print('h: ',   h.split(' ')   ,'\n',end='  ')    # string will be splited into substrings if it finds instances of separator
    d = 'Hello World'
    x = 'World' in d    # it will check if it's given sentence in designated variable
    print('d: ',   x   ,end='  ')
    e = 'Hello World'
    y = 'World' not in d    # it will check if it's not given sentence in designated variable
    print('e: ',   y   ,end='  ')
    f = a + b    # you can add same type variables
    print('f: ',   f   ,end='  ')
    g = 'Hello World, {} times'    # we add {} if we want to add number to string variable
    z = 12
    print('g: ',   g.format(z)   ,end='  ')    # it format a string g and put in brackets given number variable

    print('\n\n  Rest of useful functions with strings: https://www.w3schools.com/python/python_strings.asp\n')
STRINGS()

LISTS_INTRO = '############################## LISTS ##############################'
print(LISTS_INTRO, '\n')

def LISTS():
    a = ['Banana', 'Apple']    # simple list
    print( a[1] )    # it'll print element depends what we want
    b = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print( b[:4])    # prints all elements to given number
    c = ["apple", "banana", "cherry", "orange", "kiwi"]
    print( c[2:])    # prints elements from given number
    d = ["apple", "banana", "cherry"]
    d[1] = 'mango'    # it change the variable in given place
    print( d ) 
    e = ["apple", "banana", "cherry"]
    print( e.append('orange') )    # it add a new element to list
    f = ["apple", "banana"]
    print( f.insert(1, "mango"))    # it too add a new element but in designated place
    # TO END
LISTS()

INPUT_INTRO = '############################## INPUT ##############################'
print(INPUT_INTRO, '\n')

def INPUT():
    a = input('Enter a value: ')
    print('a value is: '+ a)

    # CREATING ACCOUNT SIMPLE FORM
 
    setEmail = input('Enter email: ')
    setPassword = input('Enter password: ')
    accountCreated = 'Failed'

    if '@' in setEmail and '.' in setEmail:
        accountCreated = 'Succesful'
        print('Account created ' + accountCreated + ' on email: ' + setEmail + ' and password ' + setPassword)
    else:
        accountCreated = 'Failed'
        print('Something go wrong, try again!\n')
        
#INPUT()

SCHOOL2902_INTRO = '############################## SCHOOL2902 ##############################'
print(SCHOOL2902_INTRO, '\n')


# import math
# # x = int(input('Podaj liczbe: '))
# # if x == 0:
# #     print('Podaj inna liczbe')
# # elif x%2 == 0:
# #     print(str(x) + ' To liczba parzysta')
# # else:
# #     print(str(x) + ' To liczba nieparzysta')

# # a = int(input('Podaj liczbe: '))
# # if a%3==0:
# #     print('Liczba jest podzielna przez 3')
# # elif a%5==0:
# #     print('Liczba jest podzielna przez 5')
# # elif a%3==0 and a%5==0:
# #     print('Liczba jest podzielna przez 3 i 5')
# # else:
# #     print('Podzielna przez to i to')
# def ZAD4():
#     a = int(input('Podaj liczbe a: '))
#     b = int(input('Podaj liczbe b: '))
#     def CheckB():
#         if b==0:
#             print('Nieskonczenie wiele rozwiazan')
#         else: 
#             print('rownanie sprzeczne')
#     if a==0:
#         CheckB()
#     else:
#         x = -(b/a)
#         print(x)    


# def ZAD5():
#     year = int(input('Podaj rok: '))
#     if year%4==0 and not year%100==0 or year%400==0:
#         print('Jest przestepny')
#     else:
#         print('Nie jest przestepny')


# def ZAD6():
#     c = int(input('Podaj liczbe c: '))
#     if c<23:
#         print(c, 23, 56)
#     elif c>56:
#         print(23, 56, c)
#     else:
#         print(23, c, 56)

# def ZAD7():
#     a = int(input('Podaj liczbe a: '))
#     b = int(input('Podaj liczbe b: '))
#     c = int(input('Podaj liczbe c: '))

#     if a==0:
#         print('To nie jest rownanie kwadratowe')
#         exit()
#     else:
#         delta = math.sqrt(b)-(4*a*c)
#         if delta<0:
#             print('Rownanie kwadratowe nie ma perwiastkow rzeczywistych')
#             exit()
#         else:
#             if delta==0:
#                 x1 = -b/2*a
#                 x2 = x1
#             else:
#                 x1 = (-b-math.sqrt(delta))/2*a
#                 x2 = (-b+math.sqrt(delta))/2*a
#             print(x1,x2)

# #https://teams.microsoft.com/_#/pdf/viewer/teams/https:~2F~2Fliceumkozy.sharepoint.com~2Fsites~2FRozszerzenie~2FShared%20Documents~2FGeneral~2F9%20p%C4%99tle%20-%20while...pdf?threadId=19:103b364ff1004eeaa204600170f99f7f@thread.tacv2&baseUrl=https:~2F~2Fliceumkozy.sharepoint.com~2Fsites~2FRozszerzenie&fileId=1a4e3067-77c1-4048-abea-6a54a705f160&ctx=files&rootContext=items_view&viewerAction=view