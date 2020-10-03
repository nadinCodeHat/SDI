import matplotlib.pyplot as plt
from scipy.stats import binom

# n is the number of trials
n = int(input("Input the number of trials: "))
# p is the probability of success
p = float(input("Input the success probability: "))
# defining the list of r values
r_values = list(range(n + 1))
# mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values]
# printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(str(r_values[i]) + "\t" + str(dist[i]))
# Plot values
plt.bar(r_values, dist)
plt.show()
# Display MEAN, VARIANCE
print("mean = " + str(mean))
print("variance = " + str(var))
