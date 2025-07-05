import numpy as np

class MetropolisHastings:
    def __init__(self):
        self.states = []
        self.samples = []

    def algorithm(self, n = 10000, x_0 = 0):
        x_n = x_0 # initial state
        for _ in range(n):
            x_prime = self.gaussian_proposal(x_n)
            acceptance_probability = self.acceptance_probability(x_prime, x_n)
            u = self.uniform_distribution()
            if u <= acceptance_probability:
                x_n = x_prime
                state = {"value": x_n, "accepted": True}
                self.states.append(state)
            else:
                state = {"value": x_n, "accepted": False}
                self.states.append(state)
            self.samples.append(x_n)

    def uniform_distribution(self):
        return np.random.uniform(0, 1)
    
    def acceptance_probability(self, x_prime, x_n):
        ratio = self.proportional_density(x_prime) / self.proportional_density(x_n)
        return min(1, ratio)

    def gaussian_proposal(self, mean, sigma = 1):
        return np.random.normal(mean, sigma)
    
    def proportional_density(self, x):
        # Target distribution standard normal distribution for now
        return np.exp(-(x**2) / 2)