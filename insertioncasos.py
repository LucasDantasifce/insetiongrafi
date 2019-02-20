from random import randint
import matplotlib as mpl
import timeit

Dlista = [10000, 20000, 30000, 40000, 50000]
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def insertionSort(lista):
    for i in range(1,len(lista)):
        x = lista[i]
        j = i-1
        while j>=0 and x<lista[j]:
            lista[j+1] = lista[j]
            j=j-1
        lista[j+1] = x

    return lista

mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,ym, label = "Medio Tempo")
    ax.plot(x,yp, label = "Pior Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoCasos.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
  medio = geraLista(i)
  melhor = sorted(medio)
  pior = sorted(medio, reverse=True)

  MelhorCaso.append(timeit.timeit("insertionSort({})".format(melhor),setup="from __main__ import insertionSort",number=1))
  PiorCaso.append(timeit.timeit("insertionSort({})".format(pior),setup="from __main__ import insertionSort",number=1))
  MedioCaso.append(timeit.timeit("insertionSort({})".format(medio),setup="from __main__ import insertionSort",number=1))



desenhaGrafico(Dlista,MelhorCaso, MedioCaso, PiorCaso)

