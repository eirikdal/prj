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
    
    def set_layer_type(self,type):
        self.__layer_type = type
        
    def set_layer_size(self,size):
        self.__layer_size = size
    
    def set_layer_act_func(self,act):
        self.__layer_act_func = act
    
    def set_link_name_pre(self,pre):
        self.__link_name_pre = pre
    
    def set_link_name_post(self,post):
        self.__link_name_post = post
    
    def set_link_conn_top(self,top):
        self.__link_conn_top = top
        
    def set_link_conn_prob(self,prob):
        self.__link_conn_prob = prob
    
    def set_link_learn_rate(self,rate):
        self.__link_learn_rate = rate
        
    def set_link_learn_param(self,param):
        self.__link_learn_param = param
        
    def set_link_learn_rule(self,rule):
        self.__link_learn_rule = rule
        
    def setup(self):
        if (self.__link_learn_rule == RULE.OJA):
            self.__link_learn_function = OjaLearning(self.__link_learn_rate)
        elif (self.__link_learn_rule == RULE.GENERAL):
            self.__link_learn_function = GeneralHebbLearning(self.__link_learn_rate, self.__link_learn_param)
        elif (self.__link_learn_rule == RULE.CLASSICAL):
            self.__link_learn_function = ClassicalHebbLearning(self.__link_learn_rate, self.__link_learn_param)