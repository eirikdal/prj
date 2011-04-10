from ann_data import ANN, TOPOLOGY, RULE
import Layer

class ann_io:
    __data = ANN()
    
    def read(self):
        file = open("ann.txt")
    
        data = file.read()
        
        __exec_order = False
        
        while str in data.split():
            if str[0] == "begin" & str[1] == "exec_order":
                __exec_order = True
            elif str[0] == "end" & str[1] == "exec_order":
                __exec_order = False
            if not __exec_order:
                self.__parse(str)
            else:
                self.__parse_exec_order(str[0])
                
        return self.__ann_data.setup()
    
    def __init__(self):
        self.__data = ANN()
        
    def __parse_exec_order(self,s):
        self.ann_data.add_exec_order(s)   
    
    def __parse(self,str):
        s = str.split(" ")
        
        if s[0] == "layer_name":
            self.__data.set_layer_name(s[1])
        elif s[0] == "layer_type":
            self.__data.set_layer_type(s[1])
        elif s[0] == "layer_size":
            self.__data.set_layer_size(int(s[1]))
        elif s[0] == "layer_act_func":
            if s[1] == "sigmoid":
                self.__data.set_layer_act_func(Layer.sigmoid)
            elif s[1] == "dsigmoid":
                self.__data.set_layer_act_func(Layer.dsigmoid)
        elif s[0] == "link_name_pre":
            self.__data.set_link_name_pre(s[1])
        elif s[0] == "link_name_post":
            self.__data.set_link_name_post(s[1])
        elif s[0] == "link_conn_top":
            if s[1] == "full":
                self.__data.set_link_conn_top(TOPOLOGY.FULL)
            elif (s[0] == "oneone"):
                self.__data.set_link_conn_top(TOPOLOGY.ONEONE)
            elif s[0] == "triangular":
                self.__data.set_link_conn_top(TOPOLOGY.TRIANGULAR)
            elif s[0] == "stochastic":
                self.__data.set_link_conn_top(TOPOLOGY.STOCHASTIC)
        elif s[0] == "link_conn_prob":
            self.__data.set_link_conn_prob(float(s[1]))
        elif s[0] == "link_learn_rule":
            if s[1] == "general-hebb":
                self.__data.set_link_learn_rule(RULE.GENERAL)
            elif s[1] == "oja":
                self.__data.set_link_learn_rule(RULE.OJA)
        elif s[0] == "link_learn_param":
            self.__data.set_link_learn_param(float(s[1]))
        elif s[0] == "link_learn_rate":
            self.__data.set_link_learn_rate(float(s[1]))
        elif s[0] == "link_range":
            t = s[1].split(",")
            (min,max) = (t[0],t[1])
        
        
        