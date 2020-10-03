from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# μ - Mean Value
mu = int(input("Input mean value: "))
# σ - Standard Deviation
sd = int(input("Input standard deviation"))

x = random.normal(size=(mu, sd))
# print the random normal distribution
print(x)

sns.distplot(random.normal(size=(mu, sd)), hist=False)
# Plot values
plt.show()
