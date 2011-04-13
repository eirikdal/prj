from LearningRule import OjaLearning, ClassicalHebbLearning, GeneralHebbLearning

class ACTIVATION:
    SIGMOID=1
    DSIGMOID=2

class TOPOLOGY:
    ONEONE=1
    FULL=2
    TRIANGULAR=3
    STOCHASTIC=4
    
class RULE:
    OJA=0
    GENERAL=1
    CLASSICAL=2
    NONE=3

class ANN_LAYER:
    def __init__(self):
        self.__layer_name = ""
        self.__layer_type = ""
        self.__layer_size = -1
        self.__layer_act_func = ACTIVATION.SIGMOID
    
    def set_layer_name(self,name):
        self.__layer_name = name
    def get_layer_name(self):
        return self.__layer_name
    
    def set_layer_type(self,type):
        self.__layer_type = type
    def get_layer_type(self):
        return self.__layer_type
    
    def set_layer_size(self,size):
        self.__layer_size = size
    def get_layer_size(self):
        return self.__layer_size
    
    def set_layer_act_func(self,act):
        self.__layer_act_func = act
    def get_layer_act_func(self):
        return self.__layer_act_func
    
class ANN_ARC:
    def __init__(self,from_node,to_node,weight):
        print "initializing arc ",self," with from_node: ",from_node
        self.__from_node = from_node
        self.__to_node = to_node
        self.__weight = weight
    
    def get_from_node(self):
        return self.__from_node
    def get_to_node(self):
        return self.__to_node
    def get_weight(self):
        return self.__weight

class ANN_LINK:
    def __init__(self):
        self.__link_name_pre = ""
        self.__link_name_post = ""
        self.__link_conn_top = TOPOLOGY.ONEONE
        self.__link_conn_prob = ""
        self.__link_learn_rate = ""
        self.__link_learn_rule = ""
        self.__link_learn_param = 0.3
        self.__link_range = (0,1)
        self.__link_arcs = []
    
    def set_link_name_pre(self,pre):
        self.__link_name_pre = pre
    def get_link_name_pre(self):
        return self.__link_name_pre
    
    def set_link_name_post(self,post):
        self.__link_name_post = post
    def get_link_name_post(self):
        return self.__link_name_post
    
    def set_link_conn_top(self,top):
        self.__link_conn_top = top
    def get_link_conn_top(self):
        return self.__link_conn_top
        
    def set_link_conn_prob(self,prob):
        self.__link_conn_prob = prob
    def get_link_conn_prob(self):
        return self.__link_conn_prob
    
    def set_link_learn_rate(self,rate):
        self.__link_learn_rate = rate
    def get_link_learn_rate(self):
        return self.__link_learn_rate
        
    def set_link_learn_param(self,param):
        self.__link_learn_param = param
    def get_link_learn_param(self):
        return self.__link_learn_param
        
    def set_link_learn_rule(self,rule):
        self.__link_learn_rule = rule
    def get_link_learn_rule(self):
        return self.__link_learn_rule
    
    def set_link_range(self,(min,max)):
        self.__link_range = (min,max)
    def get_link_range(self):
        return self.__link_range
    
    def add_arc(self, arc):
        self.__link_arcs.append(arc)
    def get_arcs(self):
        return self.__link_arcs

class ANN:
    def __init__(self):
        self.__layers = []
        self.__links = []
        self.__exec_order = []
        self.__hard_wired = False
        
        self.range = (0,0)
    
    def set_hard_wired(self,hard):
        self.__hard_wired = hard
    def get_hard_wired(self):
        return self.__hard_wired
        
    def add_link(self,link):
        self.__links.append(link)
    
    def add_layer(self,layer):
        self.__layers.append(layer)
        
    def add_exec_order(self,order):
        self.__exec_order.append(order)
    
    def get_links(self):
        return self.__links
    
    def get_layers(self):
        return self.__layers
    
    def get_exec_order(self):
        return self.__exec_order