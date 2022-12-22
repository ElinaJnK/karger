import q1c as p
import matplotlib.pyplot as plt
import time

def  trace_courbe(nb_sommets, temps_complet, temps_cycle, temps_biparti, temps_alea):
	# Plot some numbers:
	fig, ax = plt.subplots()
	complet, = ax.plot(nb_sommets, temps_complet, label='complet') 
	cycle, = ax.plot(nb_sommets, temps_cycle, label='cycle')
	biparti, = ax.plot(nb_sommets, temps_biparti, label='biparti')
	alea, = ax.plot(nb_sommets, temps_alea, label='alea')

	plt.title("Temps de calcul en fonction du nombre de sommets") 
	ax.legend([complet, cycle, biparti, alea], ['complet', 'cycle', 'biparti', 'alea'])
	# Display the plot:
	plt.show()

def test():
	nb_sommets = [i for i in range(10, 100, 10)]
	temps_complet = []
	temps_cycle = []
	temps_biparti = []
	temps_alea = []

	for n in nb_sommets:
		g_complet = p.matrice_complet(n)
		g_cycle = p.matrice_cycle(n)
		g_biparti = p.matrice_biparti(n)
		g_alea = p.matrice_alea(n, 0.8)

		t1 = time.time()
		p.algo_karger(g_complet, n)
		t2 = time.time()
		temps_complet.append(t2 - t1)

		t1 = time.time()
		p.algo_karger(g_cycle, n)
		t2 = time.time()
		temps_cycle.append(t2 - t1)

		t1 = time.time()
		p.algo_karger(g_biparti, n)
		t2 = time.time()
		temps_biparti.append(t2 - t1)

		t1 = time.time()
		p.algo_karger(g_alea, n)
		t2 = time.time()
		temps_alea.append(t2 - t1)

	trace_courbe(nb_sommets, temps_complet, temps_cycle, temps_biparti, temps_alea)

test()
