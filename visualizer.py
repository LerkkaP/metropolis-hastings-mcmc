import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    @staticmethod
    def trace_plot(samples, n = 1000):
        fig, ax = plt.subplots()
        ax.plot(range(len(samples)), samples)  
        plt.savefig("trace_plot.png")  
        
    def histogram():
        pass