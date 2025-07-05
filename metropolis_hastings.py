import numpy as np

class MetropolisHastings:
    def algorithm(self, n = 10000, x_0 = 0):
        x_n = x_0 # initial state
        states = []
        for _ in range(n):
            x_prime = self._gaussian_proposal(x_n)
            acceptance_probability = self._acceptance_probability(x_prime, x_n)
            u = self._uniform_distribution()
            if u <= acceptance_probability:
                x_n = x_prime
            states.append(x_n)
        return states

    def _uniform_distribution(self):
        return np.random.uniform(0, 1)
    
    def _acceptance_probability(self, x_prime, x_n):
        ratio = self._proportional_density(x_prime) / self._proportional_density(x_n)
        return min(1, ratio)

    def _gaussian_proposal(self, mean, sigma = 1):
        return np.random.normal(mean, sigma)
    
    def _proportional_density(self, x):
        # Target distribution standard normal distribution for now
        return np.exp(-(x**2) / 2)