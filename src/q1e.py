import random
import copy
import numpy as np
#Representons notre multigraphe en tant qu'une liste d'adjacence
def	g_complet(n):
	g = dict()
	for i in range(n):
		g[i] = [j for j in range(n) if j != i]
	return g

def	g_cycle(n):
	g = dict()
	if (n == 2):
		g[0] = [1]
		g[1] = [0]
	g[0] = [1, n - 1]
	for i in range(1, n - 1):
		g[i] = [i - 1, i + 1]
	g[n - 1] = [0, n - 2]
	return g

def	g_biparti(n):
	g = dict()
	for i in range(n // 2):
		g[i] = [j for j in range(n // 2, n) if j != i]
	for i in range(n // 2, n):
		g[i] = [j for j in range(n // 2) if j != i]
	return g

#Question 1-e :
def contraction(g, a):
	i, j = a
	# verifier si un des sommets est une instance de type int
	if isinstance(i, int) and isinstance(j, int):
		key = (i, j)
	elif isinstance(i, int) and not isinstance(j, int):
		L = list(j)
		L.append(i)
		key = tuple(set(L))
	elif isinstance(j, int) and not isinstance(i, int):
		L = list(i)
		L.append(j)
		key = tuple(set(L))
	else:
		key = tuple(set(i).union(set(j)))
	# rajout de tuple des sommets contractes qui correspond au nouveau sommet contracte
	g[key] = list(set(g[i] + g[j]))
	# suppression des aretes avec les sommets eux-memes contractes
	if i in g[key]:
		g[key].remove(i)
	if j in g[key]:
		g[key].remove(j)
	# suppression des sommets contractes
	del g[i]
	del g[j]
	
	# parcourir tous les sommets et update les values (aretes) de chaque sommet
	for som in list(g.keys()):
		for som_j in range(len(g[som])):
			if g[som][som_j] == i or g[som][som_j] == j:
				g[som][som_j] = key
	return g

# update la liste des aretes disponibles
def	update_aretes(g):
	aretes_dispo = []
	# parcours des sommets du graphe
	for key in g.keys():
		# parcours des aretes de chaque sommet
		for value in g[key]:
			# rajout de l'arete
			if (key, value) not in aretes_dispo and (value, key) not in aretes_dispo:
				aretes_dispo.append((key, value))
	return aretes_dispo

# compter le nombre de coupes a partir de l'ensemble
def	taille_coupe(g, sommets):
	# si dans sommets on a un seul sommet
	if isinstance(sommets, int):
		return len(g[sommets])

	# sinon on parcours tous les sommets
	l = []
	for som in sommets:
		for s in g[som]:
			if s not in sommets:
				l.append(s)
	return len(l)

def	arete_alea(aretes):
	a = random.choice(aretes)
	return a

def	algo_karger(g):
	gi = copy.deepcopy(g)
	n = len(g)

	while (n > 2):
		aretes_dispo = update_aretes(gi)
		a = arete_alea(aretes_dispo)
		gi = contraction(gi, a)
		n -= 1
	# on prend l'un des ensembles des sommets pour calculer la taille de la coupe de g
	sommets = list(gi.keys())
	coupe = taille_coupe(g, sommets[0])
	return (sommets[0], coupe)

#Exercice 2 :

#Question 2-b :
def	algo_karger_itere(g, T):
	m_star = np.inf
	S_star = set()

	for i in range(T):
		gi = copy.deepcopy(g)
		n = len(gi)
		while (n > 2):
			aretes_dispo = update_aretes(gi)
			a = arete_alea(aretes_dispo)
			gi = contraction(gi, a)
			n -= 1
		# on prend l'un des ensembles des sommets pour calculer la taille de la coupe de g
		sommets = list(gi.keys())
		# m : cardinal de la coupe (S, V\S)
		m = taille_coupe(g, sommets[0])
		# S : { sommets qui "apparaissent" dans v1 }
		S = sommets[0]
		if m < m_star:
			S_star = S
			m_star = m
	return (S_star, m_star)

"""
# Tests
g = {	
		0: [1, 2, 3, 4], 
		1: [0, 2, 3, 4], 
		2: [0, 1, 3, 4], 
		3: [0, 1, 2, 4], 
		4: [0, 1, 2, 3]
	}

s, m =  algo_karger(g)
print("algo Karger: ", s, m)
"""
#print("algo Karger itere: ", algo_karger_itere(g, 100))
"""
gi = copy.deepcopy(g)
print("graph : ", gi)
contraction(gi, (1, 3))
print("graph : ", gi)
contraction(gi, (0, 4))
print("graph : ", gi)
contraction(gi, (2, (1, 3)))
print("graph : ", gi)
"""
"""
contraction(gi, (1, 2))
contraction(gi, (4, 0))
contraction(gi, (3, (4, 0)))
contraction(gi, (1, 4))
contraction(gi, (0, (1, 4)))
contraction(gi, (3, (1, 4)))
print((list(gi.keys()))[0])
"""

"""
g = g_cycle(5)
print(g)
sommets, coupe = algo_karger(g)
print("sous-ens : ", sommets)
print("coupe : ", coupe)
print(g)
"""