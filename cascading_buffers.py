import random
import math

class CascadingBuffersCounter:
    def __init__(self, epsilon, d, threshold, kappa):
        self.epsilon = epsilon
        self.d = d
        self.threshold = threshold
        self.kappa = kappa
        self.accs = [self.generate_laplace_noise(1/epsilon) for _ in range(d)]
        self.buffers = [0] * d #array declaration
        self.updates = [0] * d

    def generate_laplace_noise(self, scale):
        return random.uniform(-scale, scale)

    def flush_buffer(self, level):
        if level < self.d:
            self.buffers[level + 1] += self.accs[level]
            self.flush_buffer(level + 1)
        self.buffers[level] = 0
        self.accs[level] = self.generate_laplace_noise(1/self.epsilon)
        self.updates[level] = 0

    def update(self, x):
        for i in range(len(x)):
            self.buffers[0] += x[i] + self.generate_laplace_noise(1/self.epsilon)
            self.updates[0] += 1
            if self.buffers[0] >= self.threshold or self.updates[0] == (self.threshold * self.epsilon / (4 * self.kappa)) ** 2:
                self.flush_buffer(0)

    def get_output(self):
        return sum(self.accs) 

# Example usage:
epsilon = 0.1
d = 3
threshold = 100
kappa = 0.1
cbc = CascadingBuffersCounter(epsilon, d, threshold, kappa)
x = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]  # Example input stream
cbc.update(x)
print("Output:", abs(cbc.get_output()))
