'''
Created on 8. apr. 2011

@author: hauk184
'''
import math

def sigmoid(self, x):
    return math.tanh(x)

def dsigmoid(self, y):
    return 1.0 - y**2

class Layer(object):
    nodes = []
    activation_function = sigmoid
    links_in = []
    links_out = []
    learning_mode = False
    quiescent_mode = False
    active_mode = False #Indicating whether or not the layer is currently able to a) update its neuron activation levels, and b) send those signals downstream neurons
    max_settling_rounds = 0
    
    def __init__(selfparams):
        '''
        Constructor
        '''
        