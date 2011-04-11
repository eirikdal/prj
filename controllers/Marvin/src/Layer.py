import math

from ann_data import ANN_LAYER
from Node import Node
from LearningRule import LearningFunction

def sigmoid(x):
    return math.tanh(x)

def dsigmoid(y):
    return 1.0 - y**2

class TYPE:
    INPUT = 0
    HIDDEN = 1
    OUTPUT = 2

class Layer(object):
    def __init__(self,ann_layer):
        self.__nodes = []
        self.__links_in = []
        self.__links_out = []
        self.__learning_mode = True
        self.__quiescent_mode = False
        self.__active_mode = True #Indicating whether or not the layer is currently able to a) update its neuron activation levels, and b) send those signals downstream neurons
        self.__max_settling_rounds = 1
        self.__activation_function = ann_layer.get_layer_act_func()
        self.__name = ann_layer.get_layer_name()
        self.__size = ann_layer.get_layer_size()
        for i in range(self.__size):
            self.__nodes.append(Node(self))
        self.__type = ann_layer.get_layer_type()
        
    def printout(self):
        print "Layer: " + self.get_name()
        print "Learning mode: ", self.__learning_mode
        print "Quiescent mode: ", self.__quiescent_mode
        print "Active mode: ", self.__active_mode
        print "Number of nodes: ", self.__size
        
    def printNodes(self):
        print [self.__nodes]
        
    def init_input(self,input):
        for i in range(len(input)):
            self.__nodes[i].setMembranePotential(float(input[i]))
            self.__nodes[i].setActivationLevel(float(input[i]))
        print "Layer: Input layer:"
        self.print_nodes()
            
    def get_output(self):
        return [node.getActivationLevel() for node in self.__nodes]
    
    def print_nodes(self):
        print [node.getActivationLevel() for node in self.__nodes]
 
    def reset_nodes(self):
        for i in range(self.__nodes.__len__()):
            self.__nodes[i].reset()
        
    def execute(self):
        __sum = 0
        print "Layer: Executing layer: " + self.get_name()
        if(not self.__quiescent_mode and self.__active_mode and self.__learning_mode):
            for node in self.__nodes:
                #print "Layer: num links: ", len(self.__links_in)
                for link in self.__links_in:
                    __sum += link.getOutWeights(node)
                node.setMembranePotential(__sum)
                node.setActivationLevel(self.__activation_function(__sum))
        
  
    def get_type(self):
        return self.__type
    
    def add_link_in(self, link):
        self.__links_in.append(link)
    
    def add_link_out(self,link):
        self.__links_out.append(link)
        
    def set_max_settlings_rounds(self, i):
        self.__max_settling_rounds = i
        
    def add_node(self, node):
        self.__nodes.append(node)
        
    def set_active(self, active):
        self.__active_mode = active
        
    def is_active(self):
        return self.__active_mode
    
    def is_learning(self):
        return self.__learning_mode
    
    def set_learning(self, learning):
        self.__learning_mode = learning
        
    def set_quiescent(self,quiescent):
        self.__quiescent_mode = quiescent
    
    def get_quiescent(self):
        return self.__quiescent_mode
    
    def get_linksout(self):
        return self.__links_out
    
    def get_nodes(self):
        return self.__nodes
    
    def get_name(self):
        return self.__name
    
    def remove_node(self, node):
        self.__nodes.remove(node)
