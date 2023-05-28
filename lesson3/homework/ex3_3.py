import math as m

n = 2022
x = m.pi
word = "Python"
polish = "książka"

with open('results.txt', 'w') as outfile:
    outfile.write("{}\n{}\n{}\n{}".format(n, round(x, 2), word, polish))

with open('results.txt', 'r') as infile:
    text = infile.read()

print(text)