import ann_data
import Layer

class ann_io():
    ann_data = ann_data.ANN()
    
    def __init__(self):
        self
        
    def __parse_exec_order(self,s):
        self.ann_data.add_exec_order(s)   
    
    def __parse(self,str):
        s = str.split(" ")
        
        if s[0] == "layer_name":
            ann_data.set_layer_name(s[1])
        elif s[0] == "layer_type":
            ann_data.set_layer_type(s[1])
        elif s[0] == "layer_size":
            ann_data.set_layer_size(int(s[1]))
        elif s[0] == "layer_act_func":
            if s[1] == "sigmoid":
                ann_data.set_layer_act_func(Layer.sigmoid)
            elif s[1] == "dsigmoid":
                ann_data.set_layer_act_func(Layer.dsigmoid)
        elif s[0] == "link_name_pre":
            ann_data.set_link_name_pre(s[1])
        elif s[0] == "link_name_post":
            ann_data.set_link_name_post(s[1])
        elif s[0] == "link_conn_top":
            if s[1] == "full":
                ann_data.set_link_conn_top(ann_data.TOPOLOGY.FULL)
            elif (s[0] == "oneone"):
                ann_data.set_link_conn_top(ann_data.TOPOLOGY.ONEONE)
            elif s[0] == "triangular":
                ann_data.set_link_conn_top(ann_data.TOPOLOGY.TRIANGULAR)
            elif s[0] == "stochastic":
                ann_data.set_link_conn_top(ann_data.TOPOLOGY.STOCHASTIC)
        elif s[0] == "link_conn_prob":
            ann_data.set_link_conn_prob(float(s[1]))
        elif s[0] == "link_learn_rule":
            if s[1] == "general-hebb":
                ann_data.set_link_learn_rule(ann_data.RULE.GENERAL)
            elif s[1] == "oja":
                ann_data.set_link_learn_rule(ann_data.RULE.OJA)
        elif s[0] == "link_learn_param":
            ann_data.set_link_learn_param(float(s[1]))
        elif s[0] == "link_learn_rate":
            ann_data.set_link_learn_rate(float(s[1]))
        elif s[0] == "link_range":
            t = s[1].split(",")
            (min,max) = (t[0],t[1])
    
    def read(self):
        file = open("ann.txt")
    
        data = file.read()
        
        exec_order = False
        
        while str in data.split():
            if str[0] == "begin" & str[1] == "exec_order":
                exec_order = True
            elif str[0] == "end" & str[1] == "exec_order":
                exec_order = False
            if not exec_order:
                self.__parse(str)
            else:
                self.__parse_exec_order(str[0])
                
        self.ann_data.setup()
                
    def get_ann_data(self):
        return self.ann_data
        
        
        