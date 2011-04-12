class Node:
    __layer = [] # layer in which the node resides
    __membranePotential = 0 # simplest version: sum of the weighted inputs
    __activationLevel = 0
    __prevActivationLevel = 0
    
    def __init__(self,layer):
        self.__layer = layer
        
    def getActivationLevel(self):
        return self.__activationLevel
    def setActivationLevel(self, activationLevel):
        self.__prevActivationLevel = self.__activationLevel
        self.__activationLevel = activationLevel
    
    def getPrevActivationLevel(self):
        return self.__prevActivationLevel
    
    def getMembranePotential(self):
        return self.__membranePotential
    
    def getLayer(self):
        return self.__layer
    
    def setLayer(self,layer):
        self.__layer = layer
        
    def setMembranePotential(self, membranePot):
        self.__membranePotential = membranePot
        
    def get_delta(self):
        return self.__delta
    def set_delta(self, delta):
        self.__delta = delta
    def reset_delta(self):
        self.__delta = 0
        self.__delta_backup = 0
        
    def get_delta_backup(self):
        return self.__delta_backup
    def add_delta_backup(self, backup):
        self.__delta_backup += backup