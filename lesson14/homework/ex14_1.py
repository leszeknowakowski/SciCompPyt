import numpy as np
import matplotlib.pyplot as plt
from numba import njit, int64, float64
import random
import time

##############   no numba part #################
def generate_pairs(n):
    '''generate n random points coordinates'''
    points = np.empty((n, 2))
    for i in range(n):
        x, y = random.random(), random.random()
        points[i] = x, y
    return points

def find_pi(pts):
    '''count how many points are inside a quadrant'''
    x = pts[:, 0]
    y = pts[:, 1]
    pi_num = 0
    counter = 0
    col = []
    dist = np.sqrt(x ** 2 + y ** 2)

    for d in dist:
        if d < 1:
            counter += 1
            col.append('green')
        else:
            col.append('red')
    pi_num = counter / pts.shape[0] * 4
    return pi_num

############### numba part   #########################
@njit(float64[:, :](int64))
def generate_pairs_numba(n):
    '''generate n random points coordinates'''
    points = np.empty((n, 2))
    for i in range(n):
        x, y = random.random(), random.random()
        points[i] = x, y
    return points


@njit(float64(float64[:, :]))
def find_pi_numba(pts):
    '''count how many points are inside a quadrant'''
    x = pts[:, 0]
    y = pts[:, 1]
    pi_num = 0
    counter = 0
    col = []
    dist = np.sqrt(x ** 2 + y ** 2)

    for d in dist:
        if d < 1:
            counter += 1
            col.append('green')
        else:
            col.append('red')
    pi_num = counter / pts.shape[0] * 4
    return pi_num

def timing(num):
    start_numba = time.time()
    pi_numba = find_pi_numba(generate_pairs_numba(num))
    stop_numba = time.time()
    print("\033[33mnumba:   estiamted time: {0:.6f}, pi: {1:.4f}, numbers used: {2}\033[0m".format(
        stop_numba - start_numba, pi_numba, num))
    start_reg = time.time()
    pi_reg = find_pi(generate_pairs(num))
    stop_reg = time.time()
    print("regular: estiamted time: {0:.6f}, pi: {1:.4f}, numbers used: {2}".format(stop_reg - start_reg, pi_reg, num))
    return num, stop_numba - start_numba, stop_reg - start_reg


lst = []
for n in [10 ** x for x in range(1, 7)]:
    lst.append(timing(n))

lst = np.array(lst)


plt.scatter(lst[:, 0], lst[:, 1], label='numba')
plt.scatter(lst[:, 0], lst[:, 2], label='regular')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("numbers used for simulation")
plt.ylabel("time consumed / s")
legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.show()
