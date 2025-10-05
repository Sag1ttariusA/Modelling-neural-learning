import random

class Primary_Neuron: 
    def __init__(self, name, firing_prob):            
    # firing_prob is the default probability of the neuron firing, the multiplier increases the probability of firing if other neurons are activated
        self.name = name
        self.firing_prob = firing_prob
        self.resting_prob = 1 - firing_prob
        self.result = ""
        self.spike = 0

    def simulate(self):
        self.result = random.choices(["Fires", "Rests"], weights=[self.firing_prob, self.resting_prob])[0]
    # the spike can either be 100 or 0 but nothing in between -> as far as I understood this is how neurons operate
        if self.result == "Fires":
            self.spike = 100
        else: 
            self.spike = 0
        return f"{self.name}: {self.result}"

class Secondary_Neuron:
    def __init__(self, name, resting_potential, threshold, post_fire_potential=-100):       
        self.name = name
        self.membrane_potential = resting_potential
        self.threshold = threshold
        self.post_fire_potential = post_fire_potential
        self.consecutive_rest = 0
       
    def simulate(self, signal):
        self.membrane_potential += signal

    # if the neuron reaches threshold it fires and its membrane potential is set back down
        if self.membrane_potential >= self.threshold:
            temp = self.membrane_potential
            self.membrane_potential = self.post_fire_potential
            return f"{self.name}: {temp} --> Fires!"
        elif signal < 0: 
            return f"{self.name}: {self.membrane_potential} --> Inhibited"
        else:
            return f"{self.name}: {self.membrane_potential} --> Rests"        

# We're trying to have all of the processing of the signal from the primary neurons happen in the Synapse Class, such that the secondary neurons already receive
# the processed signal
class Synapse: 
    def __init__(self, presynpatic_neuron, postsynaptic_neuron, strength, inhibitor):
        self.presynaptic_neuron = presynpatic_neuron
        self.postsynaptic_neuron = postsynaptic_neuron
        self.strength = strength  # this parameter adjusts how strong the signal from the primary neurons to the secondary will be -> 1 means 1 by 1 transport 
        self.inhibitor = inhibitor # adjusts how strong an inhibitory signal will be -> if primary neuron does not fire twice consecutively
        self.consecutive_rest = 0  # reset counter
        
    def get_signal(self):
        input = self.presynaptic_neuron.spike
        if input == 100:
            self.consecutive_rest = 0
            signal = input*self.strength
            return signal
        else:
            self.consecutive_rest += 1
        # prevent the potential from decreasing at a certain limit
            if self.postsynaptic_neuron.membrane_potential <= -100: 
                self.consecutive_rest = 0
            if self.consecutive_rest >= 2:  # only decrease after 2 rests in a row
            # this seems still somewhat hardcoded -> can you improve it?
                signal = 100*self.inhibitor
                self.consecutive_rest = 0  # reset so it requires two more rests again
            else: 
                signal = 0
            return signal
            
neuron_a = Primary_Neuron("Neuron_A", 0.4)
neuron_b = Secondary_Neuron("Neuron_B", -60, 10)
syn_a_b = Synapse(neuron_a, neuron_b, strength=0.2, inhibitor=-0.2)

def first():
    neuron_a_outpout = neuron_a.simulate()
    signal = syn_a_b.get_signal()
    neuron_b_output = neuron_b.simulate(signal)
    output = [neuron_a_outpout, neuron_b_output]
    print(output)

# for _ in range(10): 
#     first()
    
primary_neuron_a = Primary_Neuron("Primary_Neuron_A", 0.4)
primary_neuron_b = Primary_Neuron("Primary_Neuron_B", 0.4)
primary_neurons = [primary_neuron_a, primary_neuron_b]
secondary_neuron_c = Secondary_Neuron("Secondary_Neuron_C", -60, 10)
secondary_neuron_d = Secondary_Neuron("Secondary_Neuron_D", -60, 10)
secondary_neurons = [secondary_neuron_c, secondary_neuron_d]
syn_a_c = Synapse(primary_neuron_a, secondary_neuron_c, strength=0.2, inhibitor=-0.2)
syn_a_d = Synapse(primary_neuron_a, secondary_neuron_d, strength=0.2, inhibitor=-0.2)
syn_b_c = Synapse(primary_neuron_b, secondary_neuron_c, strength=0.2, inhibitor=-0.2)
syn_b_d = Synapse(primary_neuron_b, secondary_neuron_d, strength=0.2, inhibitor=-0.2)
synapses = [syn_a_c, syn_a_d, syn_b_c, syn_b_d]

def network():
    signal_c = 0
    signal_d = 0 
    outputs = []
    for neuron in primary_neurons:
        outputs.append(neuron.simulate())
    for synapse in [syn_a_c, syn_b_c]:
        signal_c += synapse.get_signal()
    for synapses in [syn_a_d, syn_b_d]: 
        signal_d += synapse.get_signal()
    outputs.append(secondary_neuron_c.simulate(signal_c))
    outputs.append(secondary_neuron_d.simulate(signal_d))
    print(outputs)
    print(f"Signal C: {signal_c}, Signal D: {signal_d}")
    
network()
