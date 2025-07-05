import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    @staticmethod
    def trace_plot(samples):
        fig, ax = plt.subplots()
        ax.plot(range(len(samples)), samples) 

        plt.title("Trace Plot") 
        plt.xlabel("Iteration")
        plt.ylabel("State")
        plt.savefig("trace_plot.png")  

    @staticmethod    
    def histogram(states_accepted, bins = 50):
        fig, ax = plt.subplots()
        ax.hist(states_accepted, bins=bins, density=True, color='lightskyblue', edgecolor='black')
        
        x = np.linspace(min(states_accepted), max(states_accepted), 1000)
        true_density = (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
        ax.plot(x, true_density, 'r', lw=2, label='True Density')
        
        ax.set_title("Histogram of MCMC States Alongside True Density")
        ax.set_xlabel("State")
        ax.set_ylabel("Density")
        plt.savefig("histogram.png")
