import random

class SimpleCounter:
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.cumulative_sum = 0

    def update(self, x):
        self.cumulative_sum += x + random.uniform(-1/self.epsilon, 1/self.epsilon)

    def get_count(self):
        return self.cumulative_sum

# Example usage:
epsilon = 0.1  # Privacy parameter
counter = SimpleCounter(epsilon)

# Update the counter with some values
counter.update(1)
counter.update(0)
counter.update(1)

# Get the current count
count = counter.get_count()
print("Current count:", count)
