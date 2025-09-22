# Project vision
In this paper I investigate how networks of neurons learn information. Specifically I will examine the following hypothesis: Networks of neurons learn patterns by a random process. Instead the network forms random synapses or uses neural circuits that are already established and then adjust these based on predictions they make and synapse activity over time (i.e. if a synapse is frequently used it is strengthened, if its rarely used it atrophies). 
The method of investigation is a simulation of a neural network in python. In the first model n neurons are generated. Then the model will be given some part of pattern as input to which a random neuron shall respond. With more run-throughs the model will be fed more parts of the pattern and new, random neurons shall respond to this. With each run-through neurons have a certain probability of forming synapses amongst each other. Through forming random synapses and adjusting connections, the model should learn. The second component to learning should be for neurons to make random predictions. That is to say if a neurons corresponds to the D in the pattern A,B,C,D then it should get into an "excited" state when the input C is received. If D is then presented the neuron should fire "more strongly"/faster. If instead E is next received, then the synapses with that neuron will weaken. This is to test whether the hypothesis of Jeff Hawkins, that humans learn models of the world through predictions is correct or not.
The second model is similar except that this time there are already established synapses i.e. there are already neural circuits. This is to test an idea I read about in a "Spektrum der Wissenschaft" article. The authors claimed that when infants are born, the brain is *not* like a blank sheet of paper but that there are rather many neural circuits which can be used for learning and many of which atrophy away. (At least as far as I can remember). Both models should include the following parameters: 
- the number of neurons
- the number and complexity (how many neurons are connected in a circuit) pre-established neural circuits
- the strength of the excitement of a neuron when it predicts the next piece of a pattern (-> the change in membrane potential before the next run through)
- the probability of new synapses forming 
- the probability that a formed synapses atrophies
	- -> if synapses get stronger that also means that this probability of atrophying lessens

Furthermore the model must have the following properties: 
- neurons should be modeled physically accurate -> membrane potential, action potential (=spikes), etc. 
- a mechanism for feeding a pattern is needed as well as of course a suitable pattern that can be given as an input
- a set of neurotransmitters and neuromodulators (e.g. dopamine) for reward of a prediction (strengthening a synapse) or punishment (weakening a synapse)
- a feedback mechanism for the neurons -> should be easy as this feedback is just the next input 
