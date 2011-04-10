import ann_io
from ann_data import ANN
from Layer import Layer

class GenericANN:
    __ann_data = ANN()
    __layers = []
    __links = []
    
    def __init__(self):
        io = ann_io.ann_io()
        __ann_data = io.read()
        
        for i in range(__ann_data.get_layer_size()):
            layer = Layer(__ann_data)
            self.__layers.append(layer)
        