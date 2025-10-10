import neuron_classes as nc
import random
import networkx as nx 
import matplotlib.pyplot as plt

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
            "q","r","s","t","u","v","w","x","y","z"            
            ]

sensory_neurons = []
secondary_neurons = []
synapses = []
for letter in alphabet: 
   sensory_neurons.append(nc.Sensory_Neuron(f"neuron_{letter}", letter))
for i in range(10): 
    secondary_neurons.append(nc.Secondary_Neuron(f"S{i+1}"))

def run_sensory_neurons():
    # list() converts words into a list of words
    # important to convert everything to lower case -> else a neuron responding to "a" won't respond to "A"
    signal = list(input("Enter a word: ").lower())    
    print(signal)
    for letter in signal:
        for neuron in sensory_neurons: 
            neuron.simulate(letter)
            if neuron.result == "Fires":
                print(f"{neuron.name}: Fires")

run_sensory_neurons()

for sen_neuron in sensory_neurons: 
    if sen_neuron.result == "Fires":
        for s_neuron in secondary_neurons: 
            rando = random.random()
            if rando <= 0.4: 
                synapses.append(nc.Synapse(sen_neuron,s_neuron))
                
    else:
        for s_neuron in secondary_neurons:
            rando = random.random()
            if rando <= 0.1: 
                synapses.append(nc.Synapse(sen_neuron,s_neuron))

G = nx.DiGraph()
for sen_neuron in sensory_neurons:
    color = "red" if sen_neuron.result == "Fires" else "lightgray"
    G.add_node(sen_neuron.name, color=color)
for s_neuron in secondary_neurons:
    G.add_node(s_neuron.name, color="green")


for synapse in synapses: 
    sen_neuron = synapse.presynaptic_neuron.name
    s_neuron = synapse.postsynaptic_neuron.name
    # print(p_neuron, s_neuron)
    G.add_edge(sen_neuron, s_neuron)

# Extract node colors for drawing
node_colors = [data.get("color", "lightgray") for _, data in G.nodes(data=True)]
    
nx.draw_circular(G, node_color=node_colors, with_labels=True, arrows=True)
plt.savefig("image_sensory_neural_network.png")

def run_network():
    for synapse in synapses:
        signal = synapse.get_signal()
        print(synapse.postsynaptic_neuron.name, signal)
        synapse.postsynaptic_neuron.signals.append(signal)

    # for s_neuron in secondary_neurons: 
    #     print(s_neuron.name, s_neuron.signals)

    output = []
    for s_neuron in secondary_neurons: 
        output.append(s_neuron.simulate())

    for element in output: 
        print(element)

run_network()



