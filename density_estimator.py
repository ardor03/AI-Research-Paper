import random
import numpy as np

class DensityEstimator:
    def __init__(self, epsilon, alpha, beta):
        self.epsilon = epsilon
        self.alpha = alpha
        self.beta = beta
        self.M = []
        self.table = {} #dictionary declaration
        self.m = None

    def initialize(self, X):
        self.m = self.polylog(1/self.epsilon, 1/self.alpha, np.log(1/self.beta))
        self.m = min(self.m, len(X))
        self.M = random.sample(X, self.m)
        self.table = {x: random.choice([0, 1]) for x in self.M}

    def update(self, x):
        if x in self.table:
            self.table[x] = random.choices([0, 1], weights=[1/2 + self.epsilon/4, 1/2 - self.epsilon/4])[0]

    def compute_density(self):
        theta = sum(self.table[x] for x in self.M) / self.m
        laplace_noise = np.random.laplace(0, 1/(self.epsilon * self.m))
        return (4 * (theta - 1/2) / self.epsilon) + laplace_noise

    def compute_theta(self):
        theta = sum(self.table[x] for x in self.M) / self.m
        return theta

    def polylog(self, *args):
        return 10

# Example usage:
epsilon = 0.1
alpha = 0.01
beta = 0.05
X = [1, 2, 3, 4, 5]  # Example universe of elements

# Initialize the density estimator
density_estimator = DensityEstimator(epsilon, alpha, beta)
density_estimator.initialize(X)

#Example Usage
density_estimator.update(1)
density_estimator.update(3)
density_estimator.update(2)
density_estimator.update(1)
density_estimator.update(3)
# Compute the density value
density = abs(density_estimator.compute_density())
print("Theta value:", density_estimator.compute_theta())
print("Density value:", density)