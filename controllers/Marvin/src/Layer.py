import math

from ann_data import ANN_LAYER

def sigmoid(self, x):
    return math.tanh(x)

def dsigmoid(self, y):
    return 1.0 - y**2

class TYPE:
    INPUT = 0
    HIDDEN = 1
    OUTPUT = 2

class Layer(object):
    __nodes = []
    __activation_function = sigmoid
    __name = ""
    __type = TYPE.INPUT
    __size = 0
    __links_in = []
    __links_out = []
    __learning_mode = False
    __quiescent_mode = False
    __active_mode = False #Indicating whether or not the layer is currently able to a) update its neuron activation levels, and b) send those signals downstream neurons
    __max_settling_rounds = 0
    
    def __init__(self,ann_layer):
        self.__activation_function = ann_layer.get_layer_act_func()
        self.__name = ann_layer.get_layer_name()
        self.__size = ann_layer.get_layer_size()
        self.__type = ann_layer.get_layer_type()
    
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