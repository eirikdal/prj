from ann_io import ann_io
import random
from ann_data import ANN
from Layer import Layer
from Link import Link
from LearningRule import OjaLearning, ClassicalHebbLearning, GeneralHebbLearning
from ann_data import RULE

class GenericANN: 
    def get_layers(self):
        return self.__layers
    
    def get_links(self):
        return self.__links
    
    def get_exec_order(self):
        return self.__exec_order
    
    def __init__(self):
        print "GenericANN: Constructor called"
        self.__layers = []
        self.__links = []
        self.__exec_order = []
        
        print "GenericANN: Begin read from script"
        io = ann_io()
        __ann_data = io.read()
        # TODO read training data
        
        print "GenericANN: ", len(__ann_data.get_layers())
        
        random.seed()
        
        print "GenericANN: Initializing GenericANN"
        
        for ann_layer in __ann_data.get_layers():
            layer = Layer(ann_layer)
            self.__layers.append(layer)
            print "GenericANN: Added layer:"
            print "------------------------"
            layer.printout()
            print "------------------------"
        
        for ann_link in __ann_data.get_links():
            # Adding layers to links
            link = Link(ann_link, self.get_layers())
            self.__links.append(link)
            
            # Adding links to layers
            for layer in self.get_layers():
                if link.getPostLayer().get_name() == layer.get_name():
                    layer.add_link_in(link)
                elif link.getPreLayer().get_name() == layer.get_name():
                    layer.add_link_out(link)
            
            print "GenericANN: Adding link from: " + link.getPreLayer().get_name() + " to: " + \
                      link.getPostLayer().get_name()
                      
            if (ann_link.get_link_learn_rule() == RULE.OJA):
                link.setLearningRule(OjaLearning(ann_link.get_link_learn_rate()))
            elif (ann_link.get_link_learn_rule() == RULE.GENERAL):
                link.setLearningRule(GeneralHebbLearning(ann_link.get_link_learn_rate(), ann_link.get_link_learn_param()))
            elif (ann_link.get_link_learn_rule() == RULE.CLASSICAL):
                link.setLearningRule(ClassicalHebbLearning(ann_link.get_link_learn_rate()))
                
            link.connect()
        
        self.__exec_order = __ann_data.get_exec_order()
        
    def do_training(self):
        print "Training"
        
        for data in self.__training_data:
            self.getLastLayer().set_target_data(data)
        
    def getFirstLayer(self):
        for layer in self.__layers:
            if (len(layer.get_linksin()) == 0):
                return layer
            
    def getLastLayer(self):
        for layer in self.__layers:
            if (len(layer.get_linksout()) == 0):
                return layer
    def execute(self):
        print "GenericANN: Executing layers in order:", self.__exec_order
        for name in self.__exec_order:
            for layer in self.__layers:
                #print layer.get_name() + "=" + name
                if layer.get_name() == name:
                    print "GenericANN: Executing layer: " + layer.get_name()
                    layer.execute()
                    layer.print_nodes()
                    break
                
        for link in self.__links:
            link.update()