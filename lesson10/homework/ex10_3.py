import pandas as pd

atomic_names = ["hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen", "fluorine",
                "neon"]
atomic_abb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
atomic_mass = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20]

d1 = {"Name":atomic_names, "Symbol":atomic_abb, "Weight":atomic_mass}

df1 = pd.DataFrame(data=d1, index=range(1,11))

print(df1)