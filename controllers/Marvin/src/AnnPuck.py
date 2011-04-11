from AgentANN import AgentANN

'''
This is the interface to the WebANN class.
'''
class AnnPuck(AgentANN):

    def __init__(self, agent, e_thresh, nvect, cvect, svect, band, snapshow,
                   concol, ann_cycles, agent_cycles, act_noise,
                   tfile):
        print "AnnPuck constructor called"
        self.agent = agent
        self.e_thresh = e_thresh
        self.nvect = nvect
        self.cvect = cvect
        self.svect = svect
        self.band = band
        self.snapshow = snapshow
        self.concol = concol
        self.ann_cycles = ann_cycles
        self.agent_cycles = agent_cycles
        self.act_noise = act_noise
        
        AgentANN.__init__(self)
        