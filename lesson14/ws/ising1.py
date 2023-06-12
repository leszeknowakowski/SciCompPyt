#!/usr/bin/python3
#
# Ising model, 2D square lattice, nearest neighbor interactions.
# Periodic boundary conditions.

import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt


def init_spins(x, y):
    L = np.empty((x, y), dtype=np.int64)
    print ( "shape {}".format(L.shape) )   # return (x, y)
    print ( "ndim {}".format(L.ndim) )   # return 2
    print ( "size {}".format(L.size) )   # return x * y
    print ( "itemsize {}".format(L.itemsize) )   # 1
    for i in range(x):
        for j in range(y):
            L[i, j] = random.choice((-1, 1))   # random system
            #L[i, j] = 1   # ordered system
    return L

def print_spins(L):
    x, y = L.shape
    M = []
    for i in range(x):
        for j in range(y):
            M.append("+ " if L[i, j] == 1 else "- ")
            #M.append("| " if L[i, j] == 1 else "- ")
            #M.append("u " if L[i, j] == 1 else "d ")
            #M.append("o " if L[i, j] == 1 else "x ")
        M.append("\n")
    return "".join(M)

def calc_magnetization(L):
    return float(L.sum())           # sum of spins
    #return float(L.sum()) / L.size   # na jeden spin

def calc_energy1(L):
    x, y = L.shape
    J = 1.0     # spin interactions
    energy = 0
    # Sum over nearest neighbors in a periodical lattice.
    for i in range(x):
        for j in range(y):
            energy += L[i, j] * L[(i+1) % x, j]
            energy += L[i, j] * L[i, (j+1) % y]
    energy = (-1) * energy
    return energy           # total energy
    #return energy / L.size   # na jeden spin

def calc_energy2(L):
    x, y = L.shape
    energy = 0
    # Sum over nearest neighbors in a periodical lattice.
    for i in range(x):
        for j in range(y):
            # Sumuje najblizszych sasiadow.
            neighbors = ( L[(i+1) % x, j] + L[(i+x-1) % x, j]
                + L[i, (j+1) % y] + L[i, (j+y-1) % y] )
            energy += L[i, j] * neighbors
    # Kazda para sasiadow jest liczona dwa razy.
    energy = -0.5 * energy
    return energy           # total energy
    #return energy / L.size   # na jeden spin

calc_energy = calc_energy2

def mc_simulation(L, t):
    x, y = L.shape
    #n_it, warmup = 1000*L.size, 10*L.size
    n_it, warmup = 100*L.size, 10*L.size   # na poczatek
    #n_it, warmup = 10*L.size, L.size   # na poczatek
    measure = L.size   # how often make measurements (x*y)

    energy = calc_energy(L)   # starting energy
    magnet = calc_magnetization(L)   # starting magnetization
    aver_n = 0    # ile konfiguracji weszlo do sredniowania
    aver_energy = 0.0
    aver_magnet = 0.0
    for it in range(n_it):
        # pick a spin
        i = random.randrange(x)
        j = random.randrange(y)
        spin = L[i, j]
        neighbors = ( L[(i+1) % x, j] + L[(i+x-1) % x, j]
            + L[i, (j+1) % y]+ L[i, (j+y-1) % y] )
        delta_energy = spin * neighbors * 2   # tu jest stary spin!
        prob = math.exp(-delta_energy / t)
        if prob > random.random():
            L[i, j] = -spin
            energy += 2 * spin * neighbors
            magnet -= 2 * spin
        if it > warmup and it % measure == 0:
            aver_n += 1
            aver_energy += energy
            aver_magnet += magnet
    e1 = aver_energy / aver_n
    m1 = aver_magnet / aver_n
    return (e1, m1)

if __name__ == "__main__":

    size_x, size_y = 10, 10
    #size_x, size_y = 20, 20
    #size_x, size_y = 30, 30
    #size_x, size_y = 40, 40
    #size_x, size_y = 50, 50
    #size_x, size_y = 100, 100

    spin_array = init_spins(size_x, size_y)
    print ( spin_array )
    print ( print_spins(spin_array) )
    print ( "calc_energy1 {}".format(calc_energy1(spin_array)) )
    print ( "calc_energy2 {}".format(calc_energy2(spin_array)) )
    print ( "magnetization {}".format(calc_magnetization(spin_array)) )

    # Lista temperatur do zbadania.
    #t_list = np.linspace(4, 1, 7)   # 7 wartosci co 0.5
    t_list = np.linspace(4, 0.5, 36)   # 36 wartosci co 0.1
    energy_list = []
    magnet_list = []
    t_all=[]

    for t in t_list:   # petla po temperaturach
        # Symulacja dla ustalonej temperatury t.
        start = time.time()
        e1, m1 = mc_simulation(spin_array, t)
        end = time.time()
        print("# Elapsed (t={0:.1f}) = {1}".format(t, end - start))
        e1 /= spin_array.size
        m1 /= spin_array.size
        energy_list.append(e1)
        magnet_list.append(m1)
        print ( "{} {} {}".format(t, e1, m1) )
        t_all.append(end-start)
    tmean = np.mean(t_all)
    print("mean time of computation: {}".format(tmean))

    # Dalej mozna dane zapisac do pliku lub od razu zrobic rysunek.
    plt.plot(t_list, energy_list, label="energy")
    plt.plot(t_list, magnet_list, label="magnet")
    plt.title("Ising 2D")
    plt.xlabel("temperature")
    plt.ylabel("")
    plt.legend()
    plt.show()   # display a figure

# EOF
