# File:          Marvin.py
# Date:          21.03.11
# Description:   Epuck Robot, implementing a Generic ANN
# Author:        Eirik Daleng Haukedal
# Modifications: 

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
#
# or to import the entire module. Ex:
#  from controller import *
#from controller import Robot
from epuck_basic import EpuckBasic
from imagepro import column_avg
from Layer import TYPE
from AnnPuck import AnnPuck
from ann_io import read_training_data
from random import uniform
import prims1

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives EpuckBasic and so inherits all its functions
class Marvin (EpuckBasic):
    def __init__(self, tempo = 1.0, e_thresh = 125, nvect = True, cvect = True, svect = True, band = 'bw', concol = 1.0, snapshow = True,
              ann_cycles = 1, agent_cycles = 5, act_noise = 0.1, tfile = "redman4"):
        EpuckBasic.__init__(self)
        self.basic_setup() # defined for EpuckBasic 
        self.ann = AnnPuck(agent = self, e_thresh = e_thresh, nvect = nvect, cvect = cvect, svect = svect, band = band, snapshow = snapshow,
                   concol = concol, ann_cycles = ann_cycles, agent_cycles = agent_cycles, act_noise = act_noise,
                   tfile = tfile, training_rounds = 50)
        
        self.sensors = [self.getDistanceSensor('ps' + str(i)) for i in range(8)]
        for s in self.sensors: s.enable(int(self.getBasicTimeStep()))

    def long_run(self,steps = 500):
        self.ann.simsteps = steps
        self.spin_angle(prims1.randab(0,360))
        self.ann.redman_run()
        
    def enter_input(self,sensors):
        #print sensors
        for layer in self.ann.get_layers():
            if layer.get_type() == TYPE.INPUT:
                sensors = map(lambda(x): self.scaleSensor(x), sensors)
                layer.init_input(sensors)
            
    def scaleSensor(self,x):
        if(x/200 < 1): 
            return x/200
        else:
            return 0.99
                
    def get_output(self):
        for layer in self.ann.get_layers():
            if layer.get_type() == TYPE.OUTPUT:
                return layer.get_output()
    
    # User defined function for initializing and running
    # the Marvin class
    def run(self):
        # You should insert a getDevice-like function in order to get the
        # instance of a device of the robot. Something like:
        #print self.get_proximities()
        pimg = self.snapshot(False)
        print pimg
        #print "proximities: "
        #print self.get_proximities()

        training_data = read_training_data()
        self.ann.do_training(training_data)
        self.ann.stop_training()
        
        # Main loop
        while True:
            # Read the sensors:
            sens = self.get_proximities()
            
            # Process sensor data here.
            self.enter_input(sens)
            self.ann.execute()
            output = self.get_output()
            
            if self.ann.is_hardwired():
                self.set_wheel_speeds(output[0]-output[2]+uniform(0.3,0.5), output[1]-output[2]+uniform(0.3,0.5))
            else:
                self.set_wheel_speeds(output[0], output[1])
            # Enter here functions to send actuator commands, like:
            #  led.set(1)
            
            # Perform a simulation step of 64 milliseconds
            # and leave the loop when the simulation is over
            if self.step(64) == -1: break
    
    # Enter here exit cleanup code

# The main program starts from here

#from webann.py:
#controller = WebAnn(tempo = 1.0, band = 'gray')
#controller.long_run(40)

controller = Marvin()
controller.basic_setup()
controller.run()
#controller.continuous_run()
#controller.run()
