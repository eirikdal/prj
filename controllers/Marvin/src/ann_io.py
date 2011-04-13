from ann_data import ANN, TOPOLOGY, RULE, ANN_LAYER, ANN_LINK, ANN_ARC
from Layer import TYPE
import Layer

def read_training_data():
    file = open("training.txt")
    
    data = file.read()
    
    print "training_io: Begin parsing training data"
    
    training_data = []
    for strdat in data.split('\n'):
        str = strdat.split()
        if not str: continue
        
        training_data.append(([str[i] for i in range(len(str)-2)],\
                              [str[i] for i in range(len(str)-2,len(str))]))
    
    return training_data

class ann_io:    
    def read(self):
        file = open("ann.txt")
    
        data = file.read()

        __exec_order = False
        __new_layer = False
        __new_link = False
        __new_arc = False
        
        print "ann_io: Begin parsing script"

        for strdat in data.split('\n'):
            str = strdat.split()
            if not str:
                continue
            if str[0] == "begin" and str[1] == "exec_order":
                __exec_order = True
                continue
            elif str[0] == "begin" and str[1] == "layer":
                self.__layer = ANN_LAYER()
                __new_layer = True
                continue
            elif str[0] == "begin" and str[1] == "link":
                self.__link = ANN_LINK()
                __new_link = True
                continue
            elif str[0] == "begin" and str[1] == "arc":
                __new_arc = True
                continue
            elif str[0] == "end" and str[1] == "exec_order":
                __exec_order = False
                continue
            elif str[0] == "end" and str[1] == "layer":
                self.__data.add_layer(self.__layer)
                __new_layer = False
                continue
            elif str[0] == "end" and str[1] == "link":
                self.__data.add_link(self.__link)
                __new_link = False
                continue
            elif str[0] == "end" and str[1] == "arc":
                __new_arc = False
            if not __exec_order:
                self.__parse(str)
            else:
                print str[0]
                self.__parse_exec_order(str[0])
                
        return self.__data
    
    def __init__(self):
        print "ann_io constructor called"
        self.__data = ANN()
        
    def __parse_exec_order(self,s):
        self.__data.add_exec_order(s)   
    
    def __parse(self,s): 
        if s[0] == "layer_name":
            self.__layer.set_layer_name(s[1])
        elif s[0] == "layer_type":
            if s[1] == "input":
                self.__layer.set_layer_type(TYPE.INPUT)
            elif s[1] == "hidden":
                self.__layer.set_layer_type(TYPE.HIDDEN)
            elif s[1] == "output":
                self.__layer.set_layer_type(TYPE.OUTPUT)
        elif s[0] == "layer_size":
            self.__layer.set_layer_size(int(s[1]))
        elif s[0] == "layer_act_func":
            if s[1] == "sigmoid":
                self.__layer.set_layer_act_func(Layer.sigmoid)
            elif s[1] == "dsigmoid":
                self.__layer.set_layer_act_func(Layer.dsigmoid)
            elif s[1] == "right_sigmoid":
                self.__layer.set_layer_act_func(Layer.right_sigmoid)
            elif s[1] == "linear":
                self.__layer.set_layer_act_func(Layer.linear)
            elif s[1] == "plinear":
                self.__layer.set_layer_act_func(Layer.plinear)
            elif s[1] == "step":
                self.__layer.set_layer_act_func(Layer.step)
            elif s[1] == "logistical":
                self.__layer.set_layer_act_func(Layer.logistical)
        elif s[0] == "link_name_pre":
            self.__link.set_link_name_pre(s[1])
        elif s[0] == "link_name_post":
            self.__link.set_link_name_post(s[1])
        elif s[0] == "link_conn_top":
            if s[1] == "full":
                self.__link.set_link_conn_top(TOPOLOGY.FULL)
            elif (s[1] == "oneone"):
                self.__link.set_link_conn_top(TOPOLOGY.ONEONE)
            elif s[1] == "triangular":
                self.__link.set_link_conn_top(TOPOLOGY.TRIANGULAR)
            elif s[1] == "stochastic":
                self.__link.set_link_conn_top(TOPOLOGY.STOCHASTIC)
        elif s[0] == "link_conn_prob":
            self.__link.set_link_conn_prob(float(s[1]))
        elif s[0] == "link_learn_rule":
            if s[1] == "general-hebb":
                self.__link.set_link_learn_rule(RULE.GENERAL)
            elif s[1] == "classical-hebb":
                self.__link.set_link_learn_rule(RULE.CLASSICAL)
            elif s[1] == "oja":
                self.__link.set_link_learn_rule(RULE.OJA)
            elif s[1] == "none":
                self.__link.set_link_learn_rule(RULE.NONE)
        elif s[0] == "link_learn_param":
            self.__link.set_link_learn_param(float(s[1]))
        elif s[0] == "link_learn_rate":
            self.__link.set_link_learn_rate(float(s[1]))
        elif s[0] == "link_range":
            t = s[1].split(",")
            (min,max) = (t[0],t[1])
        elif s[0] == "arc":
            t = s[1].split(",")
            from_node,to_node,weight = int(t[0]),int(t[1]),float(t[2])
            self.__link.add_arc(ANN_ARC(from_node,to_node,weight))
            
        
        