class Arc:
    __preNode = []
    __postNode = []
    __currentWeight = 0
    __initialWeight = 0
    __link = []        
    
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
    
    def getProstNode(self):
        return self.__postNode
    
    def getCurrentWeight(self):
        return self.__currentWeight
    
    def getInitialWeight(self):
        return self.__initialWeight
    
    def getLink(self):
        return self.__link
    
    def setPreNode(self, preNode):
        self.__preNode = preNode
        
    def setPostNode(self, postNode):
        self.__postNode = postNode
                
    def setCurrentWeight(self,weight):
        self.__currentWeight = weight
        
    def setInitialWeight(self,weight):
        self.__currentWeight = weight
        self.__initialWeight = weight
        
    def setLink(self, link):
        self.__link = link