import ann_io
from ann_data import ANN
from Layer import Layer
from Link import Link

class GenericANN:
    __ann_data = ANN()
    __layers = []
    __links = []
    __exec_order = []
    
    def __init__(self):
        io = ann_io.ann_io()
        __ann_data = io.read()
        
        for ann_layer in __ann_data.get_layers():
            layer = Layer(ann_layer)
            self.__layers.append(layer)
        
        for ann_link in __ann_data.get_links():
            link = Link(ann_link)
            self.__links.append(link)
            
        __exec_order = __ann_data.get_exec_order()
        
        
    def execute(self):
        for name in self.__exec_order:
            for layer in self.__layers:
                if layer.get_name() == name:
                    layer.execute()
                    for link in layer.get_linksout():
                        link.update()
                    break