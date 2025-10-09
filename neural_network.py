import neuron_classes as nc
import random
import pandas as pd 
import networkx as nx  
import matplotlib.pyplot as plt

primary_neurons = []
secondary_neurons = []
synapses = {}
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
                synapses[p_neuron.name] = s_neuron.name
                
    else:
        for s_neuron in secondary_neurons:
            rando = random.random()
            if rando <= 0.1: 
                synapses[p_neuron.name] = s_neuron.name

indices = []
indices.append(i for i in range(100))
data_frame = pd.DataFrame(synapses, indices).transpose() # we must pass an index, else we get an error

print(data_frame)

G = nx.DiGraph()
for neuron in primary_neurons:
    color = "red" if neuron.result == "Fires" else "lightgray"
    G.add_node(neuron.name, color=color)
for neuron in secondary_neurons:
    G.add_node(neuron.name, color="green")

for primary, secondary in synapses.items(): 
    G.add_edge(primary, secondary)

# Extract node colors for drawing
node_colors = [data.get("color", "lightgray") for _, data in G.nodes(data=True)]
    
nx.draw_circular(G, node_color=node_colors, with_labels=True, arrows=True)
plt.savefig("neural_network.png")



                

