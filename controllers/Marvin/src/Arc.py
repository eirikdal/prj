class Arc:
    __preNode = []
    __postNode = []
    __currentWeight = 0
    __initialWeight = 0
    __link = []
    __from = -1
    __to = -1
    
    def __init__(self, preNode, postNode, weight, link):
        self.__preNode = preNode
        self.__postNode = postNode
        self.__initialWeight = weight
        self.__currentWeight = self.__initialWeight
        self.__link = link
    
    def reset(self):
        self.currentWeight = self.initialWeight
        
    def getPreNode(self):
        return self.__preNode
    def setPreNode(self, preNode):
        self.__preNode = preNode
    
    def getPostNode(self):
        return self.__postNode
    def setPostNode(self, postNode):
        self.__postNode = postNode
    
    def getCurrentWeight(self):
        return self.__currentWeight
    def setCurrentWeight(self,weight):
        self.__currentWeight = weight
    
    def getInitialWeight(self):
        return self.__initialWeight
    
    def getLink(self):
        return self.__link
    
    def setInitialWeight(self,weight):
        self.__currentWeight = weight
        self.__initialWeight = weight
        
    def setLink(self, link):
        self.__link = link
        
    def getFrom(self):
        return self.__from
    def getTo(self):
        return self.__to
    
    def setFrom(self, fr):
        self.__from = fr
    def setTo(self, to):
        self.__to = to