import numpy as np
import random

class MetropolisHastings:
    def __init__(self):
        self.states_accepted = []
        self.states_rejected = []

    def uniform_distribution(self):
        pass
    
    def acceptance_probability(self):
        pass

    def gaussian_proposal(self, mean, sigma = 1):
        return np.random.normal(mean, sigma)