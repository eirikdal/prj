import GenericANN

from Layer import TYPE

def il(x): 
    if x.get_type() == TYPE.INPUT:
        return True
    else:
        return False

def ol(x):
    if x.get_type() == TYPE.OUTPUT:
        return True
    else:
        return False

class AgentANN(GenericANN):
    def __init__(self, sensors, motors):
        super()
        
        input_layers = filter(il,self.__layers)
        output_layers = filter(ol,self.__layers)
        
        self.__sensors = zip(sensors, input_layers)
        self.__motors = zip(motors, output_layers)
        