import math

import ann_data

def sigmoid(self, x):
    return math.tanh(x)

def dsigmoid(self, y):
    return 1.0 - y**2

class Layer(object):
    __nodes = []
    __activation_function = sigmoid
    __links_in = []
    __links_out = []
    __learning_mode = False
    __quiescent_mode = False
    __active_mode = False #Indicating whether or not the layer is currently able to a) update its neuron activation levels, and b) send those signals downstream neurons
    __max_settling_rounds = 0
    
    def __init__(self,ann_data):
        self.activation_function = act
    
    def add_link_in(self, link):
        self.links_in.append(link)
    
    def add_link_out(self,link):
        self.links_out.append(link)
        
    def set_max_settlings_rounds(self, i):
        self.max_settling_rounds = i
        
    def add_node(self, node):
        self.nodes.append(node)
        
    def set_active(self, active):
        self.active_mode = active
        
    def is_active(self):
        return self.active_mode