import random

class Primary_Neuron: 
    def __init__(self, name, firing_prob, multiplier):            
    # firing_prob is the default probability of the neuron firing, the multiplier increases the probability of firing if other neurons are activated
        self.name = name
        self.firing_prob = firing_prob
        self.resting_prob = 1 - firing_prob
        self.multiplier = multiplier
        self.result = ""

    def simulate(self):
        self.result = random.choices(["Fires", "Rests"], weights=[self.firing_prob, self.resting_prob])[0]
        return f"{self.name}: {self.result}"
    

class Secondary_Neuron:
    def __init__(self, name, resting_potential, threshold, signal_strength):       
        self.name = name
        self.membrane_potential = resting_potential
        self.threshold = threshold
        self.signal_strength = signal_strength
       
    def simulate(self, input):
        if input == "Fires":
            self.membrane_potential += self.signal_strength  
        if self.membrane_potential >= self.threshold:
            return f"{self.name}: {self.membrane_potential} --> Fires!"
        else: 
            return f"{self.name}: {self.membrane_potential} --> Rests"


def main():
    neuron_a = Primary_Neuron("Neuron_A", 1, 1.2)
    neuron_b = Secondary_Neuron("Neuron_B", -60, 10, 20)
    neuron_a_outpout = neuron_a.simulate()
    neuron_b_input = neuron_a.result
    neuron_b_output = neuron_b.simulate(neuron_b_input)
    output = [neuron_a_outpout, neuron_b_output]
    print(output)

main()
    




        