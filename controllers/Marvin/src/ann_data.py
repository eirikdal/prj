
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

class ANN():
    __layer_name = ""
    __layer_type = ""
    __layer_size = -1
    __layer_act_func = ACTIVATION.SIGMOID
    
    __link_name_pre = ""
    __link_name_post = ""
    __link_conn_top = TOPOLOGY.ONEONE
    __link_conn_prob = ""
    __link_learn_rate = ""
    __link_learn_rule = ""
    __link_learn_param = 0.3
    
    range = (0,0)
    
    def __init__(self):
        self
        
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
        return self.__layer_name
    
    def set_layer_act_func(self,act):
        self.__layer_act_func = act
    def get_layer_name(self):
        return self.__layer_name
    
    def set_link_name_pre(self,pre):
        self.__link_name_pre = pre
    def get_layer_name(self):
        return self.__layer_name
    
    def set_link_name_post(self,post):
        self.__link_name_post = post
    def get_layer_name(self):
        return self.__layer_name
    
    def set_link_conn_top(self,top):
        self.__link_conn_top = top
    def get_layer_name(self):
        return self.__layer_name
        
    def set_link_conn_prob(self,prob):
        self.__link_conn_prob = prob
    def get_layer_name(self):
        return self.__layer_name
    
    def set_link_learn_rate(self,rate):
        self.__link_learn_rate = rate
    def get_layer_name(self):
        return self.__layer_name
        
    def set_link_learn_param(self,param):
        self.__link_learn_param = param
    def get_layer_name(self):
        return self.__layer_name
        
    def set_link_learn_rule(self,rule):
        self.__link_learn_rule = rule
    def get_layer_name(self):
        return self.__layer_name
        
    def setup(self):
        if (self.__link_learn_rule == RULE.OJA):
            self.__link_learn_function = OjaRule(self.__link_learn_rate)
        elif (self.__link_learn_rule == RULE.CLASSICAL):
            self.__link_learn_function = GeneralHebbianRule(self.__link_learn_rate, self.__link_learn_param)