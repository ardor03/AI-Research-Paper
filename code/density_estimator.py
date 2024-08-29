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

# Read characters from file and remove duplicates
with open('input.txt', 'r') as file:
    X = list(set(file.read()))

# Initialize the density estimator
density_estimator = DensityEstimator(epsilon, alpha, beta)
density_estimator.initialize(X)

# Update the density estimator with each character in input.txt
with open('input.txt', 'r') as file:
    for char in file.read():
        density_estimator.update(char)

# Compute the density value
density = abs(density_estimator.compute_density())
print("Theta value:", density_estimator.compute_theta())
print("Density value:", density)
