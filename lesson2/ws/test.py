import numpy as np

lst = [list(c.encode('utf-8')) for c in "Leszek"]
lst_flat = list(np.concatenate(lst).flat)
print(lst_flat)