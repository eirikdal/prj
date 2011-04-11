import random
from ann_data import TOPOLOGY
from Arc import Arc

class Link:
    __arcs = [] # 2-dimensional array for arcs, TODO why 2D ?
    __preLayer = [] # pre-synaptic Layer
    __postLayer = [] # post-synaptic Layer
    __connectionType = TOPOLOGY.FULL
    __minWeight = 0
    __maxWeight = 0
    __learningRule = [] # subclass of LearningFunction
    __learning_mode = False
    __connectionProb = 0
    
    def __init__(self, ann_link):
        self.__connectionType = ann_link.get_link_conn_top()
        range = ann_link.get_link_range()
        self.__minWeight = range[0]
        self.__maxWeight = range[1]
        self.__connectionProb = ann_link.get_link_conn_prob()
    '''
    def __init__(self, arcs, preLayer, postLayer, connection, minWeight, maxWeight, learningRule):
        self.__arcs = arcs
        self.__connectionType = connection
        self.__learningRule = learningRule
        self.__maxWeight = maxWeight
        self.__minWeight = minWeight
        self.__preLayer = preLayer
        self.__postLayer = postLayer
    '''
        
    def connect(self):
        if (self.__connectionType == TOPOLOGY.FULL):
            for pre in self.__preLayer.get_nodes():
                for post in self.__postLayer.get_nodes():
                    weight = random.uniform(self.__minWeight, self.__maxWeight)
                    arc = Arc(pre, post, weight, self)
                    self.__arcs.append(arc)
        elif (self.__connectionType == TOPOLOGY.ONEONE):
            for i in range(self.__preLayer.get_nodes()):
                weight = random.uniform(self.__minWeight, self.__maxWeight)
                if (i < len(self.__postLayer.get_nodes())):
                    post = self.__postLayer.get_nodes()[i]
                else:
                    # removing node because no connection possible, not enough nodes in post layer
                    self.__preLayer.remove_node(self.__preLayer.get_nodes()[i])
                    
                arc = Arc(pre, post, weight, self)
                self.__arcs.append(arc)
            for i in range(len(self.__postLayer.get_nodes())-len(self.__preLayer.get_nodes())+1,len(self.__postLayer.get_nodes())-1):
                # more post than pre nodes, remove post nodes
                self.__postLayer.remove_node(self.__postLayer.get_nodes()[i])
        elif (self.__connectionType == TOPOLOGY.STOCHASTIC):
            for pre in self.__preLayer.get_nodes():
                for post in self.__postLayer.get_nodes():
                    chance = random.randint(1, 10)
                    if (chance % 2 == 0):
                        weight = random.uniform(self.__minWeight, self.__maxWeight)
                        arc = Arc(pre, post, weight, self)
                        self.__arcs.append(arc)
        elif (self.__connectionType == TOPOLOGY.TRIANGULAR):
            for i in range(self.__preLayer.get_nodes()):
                for j in range(self.__postLayer.get_nodes()):
                    if (not (i == j)):
                        weight = random.uniform(self.__minWeight, self.__maxWeight)
                        arc = Arc(pre, post, weight, self)
                        self.__arcs.append(arc)
        
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
    def setPreLayer(self, preLayer):
        self.__preLayer = preLayer
    
    def getPostLayer(self):
        return self.__postLayer
    def setPostLayer(self,postLayer):
        self.__postLayer = postLayer
    
    def getConnectionType(self):
        return self.__connectionType
    
    def getLearningRule(self):
        return self.__learningRule
    def setLearningRule(self, rule):
        self.__learningRule = rule
    
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