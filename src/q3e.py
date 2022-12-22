import q1c as e
import q3d as d
import matplotlib.pyplot as plt

def  trace_courbe(nb_sommets, suc_complet, suc_cycle, suc_biparti):
  # Plot some numbers:
  fig, ax = plt.subplots()
  complet, = ax.plot(nb_sommets, suc_complet, label='complet') 
  cycle, = ax.plot(nb_sommets, suc_cycle, label='cycle')
  biparti, = ax.plot(nb_sommets, suc_biparti, label='biparti')

  plt.title("Probabilite de succes en fonction du nombre de sommets et T") 
  ax.legend([complet, cycle, biparti], ['complet', 'cycle', 'biparti'])
  # Display the plot:
  plt.show()

def test(T, nb_sommets):
	suc_complet = []
	suc_cycle = []
	suc_biparti = []

	for n in nb_sommets:
		g_complet = e.matrice_complet(n)
		g_cycle = e.matrice_cycle(n)
		g_biparti = e.matrice_biparti(n)

		nb_complet = 0
		nb_cycle = 0
		nb_biparti = 0
		for i in range(T):
			_, coupe_complet = d.karger_stein(g_complet, g_complet)
			_, coupe_cycle = d.karger_stein(g_cycle, g_cycle)
			_, coupe_biparti = d.karger_stein(g_biparti, g_biparti)

			if (coupe_complet == n - 1):
				nb_complet += 1
			if (coupe_cycle == 2):
				nb_cycle += 1
			if (coupe_biparti == n / 2):
				nb_biparti += 1

		suc_complet.append(nb_complet / T)
		suc_cycle.append(nb_cycle / T)
		suc_biparti.append(nb_biparti / T)
		
	trace_courbe(nb_sommets, suc_complet, suc_cycle, suc_biparti)

T = 5
nb_sommets = [i for i in range(10, 100, 10)]
test(T, nb_sommets)