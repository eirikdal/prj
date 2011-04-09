class Link:
    __arcs = [] # 2-dimensional array for arcs
    __preLayer = [] # pre-synaptic Layer
    __postLayer = [] # post-synaptic Layer
    __connectionType = ConnectionType.FULL
    __minWeight = 0
    __maxWeight = 0
    __learningRule = [] # subclass of LearningFunction
    
    def __init__(self, arcs, preLayer, postLayer, connection, minWeight, maxWeight, learningRule):
        self.__arcs = arcs
        self.__connectionType = connection
        self.__learningRule = learningRule
        self.__maxWeight = maxWeight
        self.__minWeight = minWeight
        self.__preLayer = preLayer
        self.__postLayer = postLayer
        
    def getArcs(self):
        return self.__arcs
    
    def getPreLayer(self):
        return self.__preLayer
    
    def getPostLayer(self):
        return self.__postLayer
    
    def getConnectionType(self):
        return self.__connectionType
    
    def getLearningRule(self):
        return self.__learningRule
    
    def getMaxWeight(self):
        return self.__maxWeight
    
    def getMinWeight(self):
        return self.__minWeight
    
class ConnectionType:
    FULL = 0 # all pre-synaptic nodes synapse upon all post-synaptic nodes
    ONE_ONE = 1 # pre-synaptic nodes only connect to a single post-synaptic node
                # if layers are the same, every node connects to itself
    STOCHASTIC = 2 # connection assignment with probability
    TRIANGULAR = 3 # connection to all post-nodes except the node itself
    
class LearningRule:
    CLASSICAL_HEBB = 0
    GENENERAL_HEBB = 1
    OJA = 2