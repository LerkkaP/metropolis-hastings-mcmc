import numpy as np
import random

class MetropolisHastings:
    def __init__(self):
        self.states_accepted = []
        self.states_rejected = []

    def uniform_distribution(self):
        return np.random.uniform(0, 1)
    
    def acceptance_probability(self):
        pass

    def gaussian_proposal(self, mean, sigma = 1):
        return np.random.normal(mean, sigma)
    
    def proportional_density(self, x):
        # Target distribution standard normal distribution for now
        return np.exp(-(x**2) / 2)