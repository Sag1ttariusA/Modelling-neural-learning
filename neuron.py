### The first step is to create an a neuron (an object) that fires (is True) with a given probability
import random

def Neuron(name,probability):
    if probability > 1: 
        return "Please enter a probability between 0 and 1!"
    firing_prob = probability
    resting_prob = 1-probability
    event = random.choices(["Fires", "Rests"], weights=[firing_prob,resting_prob])[0]  # returns a list by default thus the "[0]"
    return_value = f"{name}: {event}"
    return return_value

def main():
    neuron_a = Neuron("Neuron_A", 0.2)
    if neuron_a == "Neuron_A: Fires":   
        neuron_b = Neuron("Neuron_B", 1)
        neuron_c = Neuron("Neuron_C", 1)
    else:
        neuron_b = Neuron("Neuron_B", 0.2)
        neuron_c = Neuron("Neuron_C", 0.2)
    output = [neuron_a, neuron_b, neuron_c]


        
    print(output)

main()