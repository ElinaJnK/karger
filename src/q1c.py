import numpy as np 
import random 
import copy
#Exercice 1 :

#Question 1-a :
def contraction(g,a):
	i, j = a 
	for k in range(len(g)):
		if (g[i][k] >= 0 and g[j][k] >= 0):
			g[i][k] = g[i][k] + g[j][k]
			g[k][i] = g[i][k]
		g[j][k] = -i - 1
		g[k][j] = -i - 1
	g[i][i] = 0
	return g

#Question 1-b :
def matrice_complet(n):
	mat =  [ [ 0 for i in range(n) ] for j in range(n) ]
	for i in range(n): 
		for j in range(n): 
			if i != j:
				mat[i][j] = 1
	return mat

def matrice_cycle(n):
	mat =  [ [ 0 for i in range(n) ] for j in range(n) ]
	for i in range(n-1):
		mat[i][i+1] = 1 
		mat[i+1][i] = 1
	mat[n-1][0]=1
	mat[0][n-1]=1 
	return mat 

def matrice_biparti(n):	  
	mat =  [ [ 0 for i in range(n) ] for j in range(n) ]
	for i in range(0, n // 2):
		for j in range(n // 2, n):
			mat [i][j] = 1
			mat [j][i] = 1
	return mat 

def matrice_alea(n , p) :
	mat =  [ [ 0 for i in range(n) ] for j in range(n) ]
	for i in range(n) : 
		rand = random.uniform(0,1)
		if rand<p : 
			j = random.randint(0, n - 1)
			while i==j: 
				j = random.randint(0,n-1)
			mat[i][j] = 1
			mat[j][i] = 1
	return mat

#Exercice 1-c:

#il faut prendre un indice i et j aleatoirement tant que on a pas de 1 à la position (i,j)

def	update_aretes(mat):
	aretes = []
	for i in range(len(mat)):
		for j in range(i + 1, len(mat)):
			if mat[i][j] >= 0 :
				aretes += [(i, j)] * mat[i][j]
	return aretes

def arete_alea(aretes):
	return random.choice(aretes)

def	update_set(mat, i, S):
	S.add(i)
	for a in range(len(mat)):
		if mat[0][a] == -i - 1:
			S.add(a)
	return

def	algo_karger(gi, n):
	g = copy.deepcopy(gi)
	S = set()

	aretes_dispo = update_aretes(g)
	a = arete_alea(aretes_dispo)
	g = contraction(g, a)
	i, j = a
	S.add(i)
	S.add(j)
	n -= 1

	aretes_dispo = update_aretes(g)
	while(n > 2 and aretes_dispo):
		# choix aleatoire d'une arete existante
		a = arete_alea(aretes_dispo)
		i, j = a
		g = contraction(g, a)
		# update des aretes disponibles
		aretes_dispo = update_aretes(g)
		if i in S and j not in S:
			update_set(g, j, S)
		if j in S and i not in S:
			update_set(g, i, S)
		n -= 1
	len_coupe = len(aretes_dispo)
	return (S, len_coupe)

# Tests
matrice_3 = [[0,1,0] , [1,0,1] , [0,1,0]]
matrice_4 = [[0,1,0,1], [1,0,1,1], [0,1,0,0], [1,1,0,0]]
matrice_6 = [[0,1,1,1,1,0] , [1,0,0,0,0,0] , [1,0,0,0,1,0] , [1,0,0,0,0,0] , [1,0,1,0,0,1], [0,0,0,0,1,0] ]
matrice_8 = [[0,1,1,0,0,0,1,1] , [1,0,0,1,1,0,1,1] , [1,0,0,1,0,0,1,1] , [0,1,1,0,1,0,1,1] , [0,1,0,1,0,1,1,1], [0,0,0,0,1,0,1,1],[1,1,1,1,1,1,0,0],[1,1,1,1,1,1,0,0] ]

#arete = (1,3)
#print(contraction(matrice_simple,arete))
#print(algo_karger(matrice_simple, 6))
#matrice_cyc = matrice_cycle(3)
#print(matrice_cyc)
#s = algo_karger(matrice_cyc, 3)
#print(s)
#print(matrice_biparti(7))