import ann_io
import random
from ann_data import ANN
from Layer import Layer
from Link import Link
from LearningRule import OjaLearning, ClassicalHebbLearning, GeneralHebbLearning
from ann_data import RULE


class GenericANN:
    __ann_data = ANN()
    __layers = []
    __links = []
    __exec_order = []
    
    def __init__(self):
        io = ann_io.ann_io()
        __ann_data = io.read()
        
        random.seed()
        
        for ann_layer in __ann_data.get_layers():
            layer = Layer(ann_layer)
            self.__layers.append(layer)
        
        for ann_link in __ann_data.get_links():
            link = Link(ann_link)
            self.__links.append(link)

            for layer in self.__layers:
                if(layer.get_name() == ann_link.get_link_name_pre):
                    link.setPreLayer(layer)
                if(layer.get_name() == ann_link.get_link_name_post):
                    link.setPostLayer(layer)
            
            if (ann_link.get_link_learn_rule() == RULE.OJA):
                link.setLearningRule(OjaLearning(ann_link.get_link_learn_rate()))
            elif (ann_link.get_link_learn_rule() == RULE.GENERAL):
                link.setLearningRule(GeneralHebbLearning(ann_link.get_link_learn_rate(), ann_link.get_link_learn_param()))
            elif (ann_link.get_link_learn_rule() == RULE.CLASSICAL):
                link.setLearningRule(ClassicalHebbLearning(ann_link.get_link_learn_rate()))
                
            link.connect()
            
        __exec_order = __ann_data.get_exec_order()
        
        
    def execute(self):
        for name in self.__exec_order:
            for layer in self.__layers:
                if layer.get_name() == name:
                    layer.execute()
                    break
                
        for link in self.__links:
            link.update()