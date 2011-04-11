class LearningFunction:
    __learningRate = 0
    
    def __init__(self, learningRate):
        self.__learningRate = learningRate
    
    def getWeightChange(self,preNode,postNode,weight):
        return 0
    
    def getLearningRate(self):
        return self.__learningRate
    
    def setLearningRate(self,learningRate):
        self.__learningRate = learningRate

class ClassicalHebbLearning(LearningFunction):
    def __init__(self, learningRate):
        LearningFunction.__init__(self, learningRate)
    
    def getWeightChange(self,preNode,postNode,weight):
        return preNode.getActivationLevel() * postNode.getActivationLevel() * self.__learningRate
    
class GeneralHebbLearning(LearningFunction):
    def __init__(self, learningRate, theta):
        LearningFunction.__init__(self, learningRate)
        self.__theta = theta
    
    def getWeightChange(self,preNode,postNode,weight):
        return self.__learningRate * \
            (preNode.getActivationLevel() - self.__theta) * \
            (postNode.getActivationLevel() - self.__theta)
            
class OjaLearning(LearningFunction):
    def __init__(self, learningRate):
        LearningFunction.__init__(self, learningRate)

    def getWeightChange(self,preNode,postNode,weight):
        return self.__learningRate * \
            (preNode.getActivationLevel() * \
             postNode.getActivationLevel() - \
             postNode.getActivationLevel()**2 * weight)