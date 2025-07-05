from metropolis_hastings import MetropolisHastings
from visualizer import Visualizer

def main():
    metropolis_hastings = MetropolisHastings()
    visualizer = Visualizer()

    states = metropolis_hastings.algorithm()
    visualizer.trace_plot(states)

if __name__ == "__main__":
    main()