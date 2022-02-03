import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.figure(figsize=(10,6))

x = np.linspace(-5, 5, 100)

p1 = sp.stats.norm(loc=-1).pdf(1)
p2 = sp.stats.norm(loc=0).pdf(1)
p3 = sp.stats.norm(loc=1).pdf(1)

plt.scatter(1, p1, s=100, c='blue', marker='v', 
         label=r"$N(x_1;\mu=-1)$={:.2f}".format(np.round(p1, 2)))
plt.scatter(1, p2, s=100, c='orange', marker='^', 
         label=r"$N(x_1;\mu=0)$={:.2f}".format(np.round(p2, 2)))
plt.scatter(1, p3, s=100, c='green', marker='s', 
         label=r"$N(x_1;\mu=1)$={:.2f}".format(np.round(p3, 2)))

plt.plot(x, norm.pdf(x,loc=-1), ls="-.")
plt.plot(x, norm.pdf(x,loc=0), ls="--")
plt.plot(x, norm.pdf(x,loc=1), ls="-")

plt.scatter(1, 0, s=100, c='k')
plt.vlines(1, -0.09, 0.45, linestyle=":")
plt.hlines(0, -5, 5, colors='gray', linestyle="-")
plt.text(1-0.3, -0.15, "$x_0=1$")

plt.xlabel("x")
plt.ylabel("likelihood")
plt.legend()
plt.title("MLE for population mean")
plt.show()

x0=1
def liklihood(x,M):
    return (1 / math.sqrt(2*math.pi) * math.pow(1, 2)) * np.exp(-(np.power(x - M, 2) / 
    (2*math.pow(1, 2))))
print('mu=-1: likelihood at x_0=1 is {:.4f}'.format(p1))
print('mu=0: likelihood at x_0=1 is {:.4f}'.format(p2))
print('mu=1: likelihood at x_0=1 is {:.4f}'.format(p3))