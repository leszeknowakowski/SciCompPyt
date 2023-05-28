import random
import matplotlib.pyplot as plt

'''infinite generator approach'''


def gen_random_walk(start):

    position = start
    counter = 0
    while True:
        rand = random.choice([-1, 1])
        position += rand
        counter += 1
        yield [position, counter]


def gen_trials(trial_num):
    final_positions = []
    for j in range(trial_num):
        positions = []
        for i in gen_random_walk(0):
            positions.append(i[0])
            if i[1] > 100:
                break
    last_position = positions[-1]
    final_positions.append(last_position)
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("Random Walker infinite generator {} trials result: ".format(trial_num))
    ax1.scatter(range(trial_num), final_positions)
    ax1.set_xlabel('trial number')
    ax1.set_ylabel('position')
    ax2.hist(final_positions, bins=20)
    ax2.set_xlabel('position')
    ax2.set_xlabel('counts')

    plt.subplots_adjust(hspace=0.5)

    return plt.show()


'''non-generator approach'''


def func_random_walk(position):

    for i in range(100):
        rand = random.choice([-1, 1])
        position += rand
    return position


def random_trials(trial_num):
    positions = []
    for i in range(trial_num):
        positions.append(func_random_walk(0))
    return positions


def random_plots(trial_num):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("Random Walker {} trials result: ".format(trial_num))
    ax1.scatter(range(trial_num), random_trials(trial_num))
    ax1.set_xlabel('trial number')
    ax1.set_ylabel('position')
    ax2.hist(random_trials(trial_num), bins=20)
    ax2.set_xlabel('position')
    ax2.set_xlabel('counts')
    plt.subplots_adjust(hspace=0.5)

    return plt.show()


gen_trials(10000)
random_plots(10000)