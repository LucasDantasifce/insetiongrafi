#from random import randint
import matplotlib as mpl
import timeit
import numpy

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
    ax.plot(x,y, label = "Pior Tempo")#Melhor Tempo
    ax.plot(x,ym, label = "Medio Tempo")#Medio Tempo
    ax.plot(x,yp, label = "Melhor Tempo")#Pior Tempo
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoCasos.png')

import itertools as it
tamlista = list(it.permutations(list(range(6))))
tempoIteracao = []
listaOrig = []
for lista in tamlista:
 tempoIteracao.append(timeit.timeit("insertionSort({})".format(list(lista).copy()),setup="from __main__ import insertionSort",number=1))
 listaOrig.append(list(lista))

print("O tempo minimo foi de {}".format(min(tempoIteracao)))
print("lista que teve tempo minimo foi:{}".format(listaOrig[tempoIteracao.index(min(tempoIteracao))]))
print("O tempo maximo foi de {}".format(max(tempoIteracao)))
print("lista que teve tempo maximo foi:{}".format(listaOrig[tempoIteracao.index(max(tempoIteracao))]))
