from metropolis import MetropolisHastings
from visualizer import Visualizer

def main():
    metropolis_hastings = MetropolisHastings()
    visualizer = Visualizer()
    states, states_accepted = metropolis_hastings.algorithm()
    
    visualizer.trace_plot(states)
    visualizer.histogram(states_accepted)

if __name__ == "__main__":
    main()