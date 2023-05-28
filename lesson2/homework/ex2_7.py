import numpy as np

roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
arabic = [ 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

D = dict(zip(roman, arabic))
print(D)

D = {}
D["I"] = 1; D["IV"] = 4; D["V"] = 5
print(D)

D = {"I":1, "IV":4, "V":5}
print(D)



