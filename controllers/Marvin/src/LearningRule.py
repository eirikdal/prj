class LearningFunction:
    __learningRate = 0
    
    def __init__(self, learningRate):
        self.__learningRate = learningRate
    
    def getWeightChange(self,preActivation,postActivation,weight):
        return 0
    
    def getLearningRate(self):
        return self.__learningRate
    
    def setLearningRate(self,learningRate):
        self.__learningRate = learningRate

class ClassicalHebbLearning(LearningFunction):
    def __init__(self, learningRate):
        LearningFunction.__init__(self, learningRate)
    
    def getWeightChange(self,preActivation,postActivation,weight):
        return preActivation * postActivation * self.getLearningRate()
    
class GeneralHebbLearning(LearningFunction):
    def __init__(self, learningRate, theta):
        LearningFunction.__init__(self, learningRate)
        self.__theta = theta
    
    def getWeightChange(self,preActivation,postActivation,weight):
        return self.getLearningRate() * \
            (preActivation - self.__theta) * \
            (postActivation - self.__theta)
            
class OjaLearning(LearningFunction):
    def __init__(self, learningRate):
        LearningFunction.__init__(self, learningRate)

    def getWeightChange(self,preActivation,postActivation,weight):
        return self.getLearningRate() * \
            (preActivation * \
             postActivation - \
             postActivation**2 * weight)