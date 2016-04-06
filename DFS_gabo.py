# -*- coding: utf-8 -*-
"""
Gabriel Novais e Gabriel Jardim
Problem 3
"""

#Transformando os dados para ficarem como dicionário:
'''with open('C:\\Users\\Samsung\\Desktop\\SCC.txt', 'r') as f:
    texto = f.read()
    lista = texto.split(" ") '''

lista=[1,2,2,3,2,4,3,1,3,9,3,11,4,5,4,6,5,7,6,5,7,6,8,7,8,10,9,6,9,8,9,10,10,11,11,9]


grafo_ex = [[1,2],[2,4],[3,5],[4,1],[4,6],[5,6],[6,3]]
#função recebe um grafo e retorna um grafo com direção das arestas invertidas
def inverte(grafo):
    for i in range(0,len(grafo)):
        (grafo[i])[0],(grafo[i])[1] = (grafo[i])[1],(grafo[i])[0]
    return(grafo)

#marca nó como explorado
def explore(no,explored):
    explored[no-1] = 1
    return(explored)



#implementação depth first search
def DFS_loop(grafo,n,t = 0,s = 0):
#cria lista que informa A[i] = 1 se nó i já foi explorado, 0 c.c.
    m = len(grafo)
    explored,lid,ft = list(range(0,n)),list(range(0,n)),list(range(0,n))
    for i in range(0,n):
        explored[i] = 0 #usar como otimização alterar somente valor de explored[2]
        lid[i] = 0
        ft[i] = 0
        
    for i in reversed(range(1,n+1)): #range dos nós (corrige o maldito inicio em 0)
        if explored[i-1] == 0:
            s = i
            DFS(grafo,m,n,i,t,s,explored,lid,ft)
    return(lid,ft)


def DFS(grafo,m,n,i,t,s,explored,lid,ft):
    explore(i,explored)
    lid[i-1] = s
#para cada nó j
    for j in range(m):
        if grafo[j][0] == i: #testa se o nó de saída é realmente o nó_i
            if explored[grafo[j][1]-1] == 0: #verifica se o nó de chegada já foi explorado
                DFS(grafo,m,n,grafo[j][1]-1,t,s,explored,lid,ft)
    t =+ 1
    ft[i]=t
    return(t,s,explored,lid,ft)
    
DFS_loop(grafo_ex,6)
