lista=[1,2,3]
print(lista)
lista.append(4)
print(lista)
lista.insert(3,5)
print(lista)
lista.remove(5)
print(lista)
lista.pop(3)
print(lista)
lista.append(2)
lista.sort()
print(lista)
lista.reverse()
lista.copy()
lista.clear()
print(lista)

----------------------------------------------
cw1
for i in range (0,15):
    lista.append((i))
print(lista)
---------------------------------------------------------------------------------------
b)
lista1=[num**5 for num in range(15)]
---------------------------------------------------------------------------------------
lista2=[math.factorial(num) for num in range(20)]
---------------------------------------------------------------------------------------
lista3=[math.e ** num for num in range(20)]
---------------------------------------------------------------------------------------
lista_nazwisk = ["Buta","Kowalski","Todorowski","Gorczynski","Nowak"]
lista4=[len(val) for val in lista4]
---------------------------------------------------------------------------------------
lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[10,20,30,40,50,60,70,80,90,100]
wynik=[]
for i in range (0,len(lista1)):
    wynik.append(lista1[i]+lista2[i])
print(wynik)
---------------------------------------------------------------------------------------
def miesiac(a):
    lista=["Styczen","Luty","Marzec",'Kwiecien',"Maj","Czerwiec","Lipiec","Sierpien","Wrzesien","Pazdziernik","Listopad","Grudzien"]
    return lista.index(a)+1
a="Kwiecien"
print(miesiac(a))
---------------------------------------------------------------------------------------
lista_nazwisk = ["Buta","Kowalski","Todorowski","Gorczynski","Nowak"]
wynik=[]
def abc(lista_nazwisk,litera):
    for nazwisko in lista_nazwisk:
        if nazwisko[0]>litera:
            wynik.append(nazwisko)
    return wynik

print(abc(lista_nazwisk,'B'))
---------------------------------------------------------------------------------------
lista_nazwisk = ["Buta","Kowalski","Todorowski","Gorczynski","Nowak"]
def funkcja3(lista_nazwisk,int):
    return [val for val in lista_nazwisk if len(val)>int]

print(funkcja3(lista_nazwisk,6))
---------------------------------------------------------------------------------------
def funkcja4(a):
    if a[::-1]==a:
        return 1
    else:
        return 0
---------------------------------------------------------------------------------------
def funkcja5(lista):
    for i in range(0,len(lista)):
        if(lista[i]>lista[i+1]):
            return True
        else:
            return False
---------------------------------------------------------------------------------------
def funkcja6(lista):
    return [val**3 for val in lista]

lista=[1,2,3]
print(funkcja5(lista))
---------------------------------------------------------------------------------------
def funkcja7(lista,n1,n2):
    for i in range(0,len(lista)):
        if lista[i]==n1:
             lista[i]=n2
    return lista

lista=[1.22,4.33,4.33,6.55]
print(funkcja7(lista,4.33,5.00))
---------------------------------------------------------------------------------------
import math
def funkcja7(lista,n1,n2):
    for i in range(0,len(lista)):
        if math.isclose(lista[i],n1):
             lista[i]=n2
    return lista
---------------------------------------------------------------------------------------
panstwa = {"Polska","Niemcy","Finlandia","Belgia","Czechy"}
-------------------------------------------------------
panstwa.add("Słowacja")
-------------------------------------------------------
'Polska' in panstwa
-------------------------------------------------------
panstwa.remove("Niemcy")
-------------------------------------------------------
panstwa|panstwa2
-------------------------------------------------------
panstwa & panstwa2
------------------------------------------------------
panstwa2 - panstwa
------------------------------------------------------
panstwa3.issubset(panstwa)
