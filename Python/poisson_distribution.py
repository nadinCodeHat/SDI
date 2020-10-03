from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# μ,λ - The mean number of successes
mu = int(input("Input μ or λ value: "))
# k,x - The actual number of successes
k = int(input("Input k or x value: "))

data_poisson = (random.poisson(mu, k))
ax = sns.distplot(data_poisson, kde=False)

plt.show()
