import neuron_classes as nc
import random
import pandas as pd 
import networkx as nx  
import matplotlib.pyplot as plt

primary_neurons = []
secondary_neurons = []
synapses = []
for i in range (5):
    primary_neurons.append(nc.Primary_Neuron(f"P{i+1}"))

for i in range(10): 
    secondary_neurons.append(nc.Secondary_Neuron(f"S{i+1}"))

for p_neuron in primary_neurons: 
    p_neuron.simulate()
    if p_neuron.result == "Fires":
        for s_neuron in secondary_neurons: 
            rando = random.random()
            if rando <= 0.4: 
                synapses.append(nc.Synapse(p_neuron,s_neuron))
                
    else:
        for s_neuron in secondary_neurons:
            rando = random.random()
            if rando <= 0.1: 
                synapses.append(nc.Synapse(p_neuron,s_neuron))

G = nx.DiGraph()
for neuron in primary_neurons:
    color = "red" if neuron.result == "Fires" else "lightgray"
    G.add_node(neuron.name, color=color)
for neuron in secondary_neurons:
    G.add_node(neuron.name, color="green")

# for primary, secondary in synapses.items(): 
#     G.add_edge(primary, secondary)

for synapse in synapses: 
    p_neuron = synapse.presynaptic_neuron.name
    s_neuron = synapse.postsynaptic_neuron.name
    # print(p_neuron, s_neuron)
    G.add_edge(p_neuron, s_neuron)

# Extract node colors for drawing
node_colors = [data.get("color", "lightgray") for _, data in G.nodes(data=True)]
    
nx.draw_circular(G, node_color=node_colors, with_labels=True, arrows=True)
plt.savefig("image_neural_network.png")

def run_network():
    for neuron in primary_neurons:
        neuron.simulate()

    for synapse in synapses:
        signal = synapse.get_signal()
        print(synapse.postsynaptic_neuron.name, signal)
        synapse.postsynaptic_neuron.signals.append(signal)

    # for s_neuron in secondary_neurons: 
    #     print(s_neuron.name, s_neuron.signals)

    output = []
    for neuron in secondary_neurons: 
        output.append(neuron.simulate())

    for element in output: 
        print(element)

run_network()
                

