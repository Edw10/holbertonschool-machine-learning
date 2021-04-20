#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
names = ["Farrah", "Fred", "Felicia"]
a = np.add(fruit[1], fruit[0])

plt.title("Number of Fruit per Person")
plt.ylabel("Quantity of Fruit")
plt.ylim(0, 80, 10)
plt.bar(names, fruit[0], 0.5, label="apples", color="red")
plt.bar(names, fruit[1], 0.5, bottom=fruit[0], label="bananas", color="yellow")
plt.bar(names, fruit[2], 0.5, bottom=np.add(fruit[1], fruit[0]), label="oranges", color="#ff8000")
plt.bar(names, fruit[3], 0.5, bottom=np.add(fruit[2], a), label="peaches", color="#ffe5b4")
plt.legend(loc='upper right')
plt.show()
