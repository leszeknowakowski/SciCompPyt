import numpy as np

## part a
lst = [list(chr.encode('utf-8')) for chr in "Leszek"]
lst_flat = list(np.concatenate(lst).flat)
print("Leszek --> ", lst_flat)

## part b
atomic_numbers = list(range(1, 11))
atomic_names = ["hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen", "fluorine",
                "neon"]
atomic_abb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
atomic_mass = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20]
headings = ["No.", "name", "symbol", "mass"]
atomic_list = np.transpose([atomic_numbers, atomic_names, atomic_abb, atomic_mass]).tolist()
atomic_list_whead = atomic_list.insert(0, headings)

def print_table(list):
    a = list[0].rjust(3) + " " + list[1].ljust(20) + list[2].center(6) + list[3].rjust(10)
    return print(a)


for i in range(len(atomic_list)):
    print_table(atomic_list[i])