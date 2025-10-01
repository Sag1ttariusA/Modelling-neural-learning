import random

class Neuron: 
    def __init__(self, name, firing_prob, multiplier):            
    # firing_prob is the default probability of the neuron firing, the multiplier increases the probability of firing if other neurons are activated
        self.name = name
        self.firing_prob = firing_prob
        self.resting_prob = 1 - firing_prob
        self.multiplier = multiplier

    @classmethod # why did it work without the decorator "@classmethod"
    def simulate(cls):
        event = random.choices(["Fires", "Rests"], weights=[self.firing_prob,self.resting_prob])[0]
        return f"{self.name}: {event}"
    
neuron_a = Neuron("Neuron_A", 0.3, 1.2)
print(neuron_a.simulate())


        