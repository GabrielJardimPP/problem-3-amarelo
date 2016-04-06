
# -*- coding: utf-8 -*-
"""
Gabriel Novais e Gabriel Jardim
Problem 3
"""

#Transformando os dados para ficarem como dicionário:
from itertools import groupby
'''with open('C:\\Users\\Samsung\\Desktop\\SCC.txt', 'r') as f:
    texto = f.read()     
    lista = texto.split(" ") '''   

lista=[1,2,2,3,2,4,3,1,3,9,3,11,4,5,4,6,5,7,6,5,7,6,8,7,8,10,9,6,9,8,9,10,10,11,11,9]
for i in range(0,len(lista)):
    lista[i]=int(lista[i])

impar=[]
par=[]
for i in range(0,len(lista)):
    if i%2==1:
        impar.append(lista[i])
    else:
        par.append(lista[i])

repeticoes=[len(list(repetidas)) for key, repetidas in groupby(par)]

vetor_auxiliar=[]
s0=0
s1=0
cont=0    
for i in range(0,len(repeticoes)):    
    s1=s1+repeticoes[i]    
    vetor_auxiliar.append(impar[s0:s1])
    s0=s0+repeticoes[i]
    
a=[]
grafo=[]
for i in range(0,len(vetor_auxiliar)):
    a.append(i+1)
    a.append(vetor_auxiliar[i])
    grafo.append(a)
    a=[]    
grafo       


'''#Construindo o DPS:
def visita(grafo):
    pre=0
    pos=0
    while i<=11
            vai=grafo[i][1][j]
            pre=pre+1'''
            
grafo_ex = [[1,2],[2,4],[3,5],[4,1],[4,6],[5,6],[6,3]]
#função recebe um grafo e retorna um grafo com direção das arestas invertidas
def inverte(grafo):
    for i in range(0,len(grafo)):
        (grafo[i])[0],(grafo[i])[1] = (grafo[i])[1],(grafo[i])[0]
    return(grafo)
    
#marca nó como explorado
def explore(nó,explored):
    explored[nó] = 1
    
#implementação depth first search
def DFS_loop(grafo,n,t = 0,s = 0):
#número de arestas(m)   
    m = len(grafo)
#cria lista que informa A[i] = 1 se nó i já foi explorado, 0 c.c.
    explored = list(range(0,n))
    for i in range(0,n):
        explored[i] = 0
        
    for i in reversed(range(n)):
        if explored[i] == 0:
            s = i
            DFS(grafo,i)
    
            

