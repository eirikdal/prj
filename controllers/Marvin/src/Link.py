from ann_data import TOPOLOGY

class Link:
    __arcs = [] # 2-dimensional array for arcs, TODO why 2D ?
    __preLayer = [] # pre-synaptic Layer
    __postLayer = [] # post-synaptic Layer
    __connectionType = TOPOLOGY.FULL
    __minWeight = 0
    __maxWeight = 0
    __learningRule = [] # subclass of LearningFunction
    __learning_mode = False
    
    def __init__(self, arcs, preLayer, postLayer, connection, minWeight, maxWeight, learningRule):
        self.__arcs = arcs
        self.__connectionType = connection
        self.__learningRule = learningRule
        self.__maxWeight = maxWeight
        self.__minWeight = minWeight
        self.__preLayer = preLayer
        self.__postLayer = postLayer
        
    def update(self):
        # in order for plasticity to occur:
        # post-synaptic layer and link of an arc must be in learning mode
        if (self.__learning_mode == True):
            for arc in self.__arcs:
                if (arc.getPreNode().getLayer().is_active() and arc.getPreNode().getLayer().is_learning()):
                    arc.setCurrentWeight(arc.getCurrentWeight() + \
                        self.__learningRule.getWeightChange(arc.getPreNode(), arc.getPostNode(), arc.getCurrentWeight()))
        
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
    
    def getOutWeights(self, node):
        sum = 0
        
        for arc in self.__arcs:
            if (arc.getPostNode() == node):
                sum += arc.getPreNode().getActivationLevel() * arc.getCurrentWeight()
                
        return sum