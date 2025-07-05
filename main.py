from metropolis_hastings import MetropolisHastings
from visualizer import Visualizer

def main():
    metropolis_hastings = MetropolisHastings()
    visualizer = Visualizer()
    metropolis_hastings.algorithm()
    samples = metropolis_hastings.samples

    visualizer.trace_plot(samples)

if __name__ == "__main__":
    main()