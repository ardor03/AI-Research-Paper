import random

class ContObsDenEst:
    def __init__(self, epsilon, alpha, beta):
        self.epsilon = epsilon
        self.alpha = alpha
        self.beta = beta
        self.table = {}  # Table to store bits for elements in M
        self.counter = 0

    def update(self, xt):
        # Generate update value yt based on the input xt
        if xt == '⊥' or xt not in self.table: #'⊥' is used in the same convention as the paper
            yt = random.randint(0, 1)  # Uniformly random bit
        else:
            bxt = self.table[xt]
            if bxt == 0:
                yt = random.choices([0, 1], weights=[1 + self.epsilon + self.epsilon*self.epsilon , 1])[0]
            else:
                yt = random.choices([0, 1], weights=[1 , 1 + self.epsilon + self.epsilon*self.epsilon])[0]
        
        # Update the counter
        self.counter += yt

        # Update the table entry for xt
        if xt not in self.table:
            self.table[xt] = random.choices([0, 1], weights=[0.5 + self.epsilon / 4, 0.5 - self.epsilon / 4])[0]

        return self.counter

# Example usage:
if __name__ == "__main__":
    epsilon = 0.1  # Privacy parameter
    alpha = 0.01   # Accuracy parameter
    beta = 0.05    # Probability parameter

    estimator = ContObsDenEst(epsilon, alpha, beta)

    # Update the estimator with some values
    for _ in range(10):
        count = estimator.update(random.choice(['⊥', '1']))

    # Get the current count
    print("Current count:", count)
