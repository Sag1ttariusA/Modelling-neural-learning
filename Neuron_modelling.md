# Modelling the neurons

- [ ] **Setting up a firing mechanism**
	- [x] have it fire at some probability otherwise have it rest
	- [x] create a function that increases the likelihood that one neuron will fire, if another fires
 	- [x] create a neuron class
  	- [x] upgrade the firing mechanism
  		- [x] neuron a that randomly fires -> primary sensory neuron
  	 	- [x] neuron b's membrane potential is increased if neuron a fires and decreased or unaltered if neuron a rests 
  	  	- [x] if neuron b's membrane potential is reached, then it fires 	

- [ ] **Storing the state of the system** 
-> the systems state should incorporate all the details which are needed to run the next step of the simulation -> state determines next run through
**-> rather than this, I implemented synapses which process the signals for the secondary neurons, such that they merely receive the signal
--> synpases determine next run through**

- [x] **Create a primitive network of neurons**
	- [x] create 2 primary neurons and 2 secondary neurons and form some connections between them, then adjust you're classes to make this work 

- [ ] **study the basics of graph theory** 
	- [x] graph theory as such 
	- [ ] how to implement graphs in python

- [ ] **increase the size of the neural network**
	- [] say 5 primary and 10 secondary neurons