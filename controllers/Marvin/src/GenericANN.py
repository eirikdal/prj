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
        
        for ann_layer in __ann_data.get_layers():
            layer = Layer(ann_layer)
            self.__layers.append(layer)
        