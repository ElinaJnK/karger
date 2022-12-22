import q1c as e
import copy
import numpy as np
import math

#Exercice 3 :

#Question 3-d :
# contraction partielle sur matrice d'adjacence
def	contraction_partielle(gi, t):
	n = len(gi)
	g = copy.deepcopy(gi)
	S = set()
	aretes_dispo = e.update_aretes(g)
	a = e.arete_alea(aretes_dispo)
	g = e.contraction(g, a)
	i, j = a
	S.add(i)
	S.add(j)
	n -= 1
	aretes_dispo = e.update_aretes(g)
	while(n > t and aretes_dispo):
		# choix aleatoire d'une arete existante
		a = e.arete_alea(aretes_dispo)
		i, j = a
		g = e.contraction(g, a)
		# update des aretes disponibles
		aretes_dispo = e.update_aretes(g)
		if i in S and j not in S:
			e.update_set(g, j, S)
		if j in S and i not in S:
			e.update_set(g, i, S)
		n -= 1
	return g

def	taille_coupe(g, s):
	return sum(g[s])

def	karger_stein(ginit, g):
	n = len(g)
	if n <= 6 or len(e.update_aretes(g)) == 0:
		m = np.inf
		s = np.inf
		for i in range(n):
			mi = 0
			for j in range(n):
				if g[i][j] >= 0:
					mi += g[i][j]
			if mi < m:
				s = i
				m = mi
		return (s, m)
	
	t = math.ceil(1 + n / math.sqrt(2))

	g1 = contraction_partielle(g, t)
	s1, _ = karger_stein(ginit, g1)
	m1 = taille_coupe(ginit, s1)

	g2 = contraction_partielle(g, t)
	s2, _ = karger_stein(ginit, g2)
	m2 = taille_coupe(ginit, s2)

	if m1 < m2:
		return (s1, m1)
	return (s2, m2)

"""
g = e.matrice_8
print(g)
s, m = karger_stein(g, g)
print(s, m)
"""