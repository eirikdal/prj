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

from AnnPuck import AnnPuck
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
                   tfile = tfile)
        
        self.sensors = [self.getDistanceSensor('sensor' + str(i)) for i in range(8)]
        for s in self.sensors: s.enable()

    def long_run(self,steps = 500):
        self.ann.simsteps = steps
        self.spin_angle(prims1.randab(0,360))
        self.ann.redman_run()
        
    def enter_input(self,sensors):
        for s in sensors:
            s.hallo()
    # User defined function for initializing and running
    # the Marvin class
    def run(self):
        # You should insert a getDevice-like function in order to get the
        # instance of a device of the robot. Something like:
        #  led = self.getLed('ledname')
        '''
        1. get_proximities(): vector with values from the 8 distance sensors
        2. snapshot()
        3. move, move_wheels, set_wheel_speeds
        4. run_timestep, do_timed_action
        '''

        # Main loop
        while True:
      
            # Read the sensors:
            # Enter here functions to read sensor data, like:
            for s in self.sensors:
                val = s.getValue()
                simg = self.get_proximities()#self.snapshot()
                pimg = self.snapshot(simg)
                
                self.show(pimg)
                self.enter_input(s)
            # Process sensor data here.
            #self.enter_input(img)
            # Enter here functions to send actuator commands, like:
            #  led.set(1)
            
            # Perform a simulation step of 64 milliseconds
            # and leave the loop when the simulation is over
            if self.step(64) == -1: break
    
    # Enter here exit cleanup code

# The main program starts from here

# This is the main program of your controller.
# It creates an instance of your Robot subclass, launches its
# function(s) and destroys it at the end of the execution.
# Note that only one instance of Robot should be created in
# a controller program.

#from webann.py:
#controller = WebAnn(tempo = 1.0, band = 'gray')
#controller.long_run(40)

controller = Marvin()
controller.basic_setup()
controller.run()
#controller.continuous_run()
#controller.run()
