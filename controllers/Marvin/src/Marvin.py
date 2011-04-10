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

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives EpuckBasic and so inherits all its functions
class Marvin (EpuckBasic):
  
    # User defined function for initializing and running
    # the Marvin class
    def run(self):
        ds = self.getDistanceSensor('Marvin')
        ds.enable()
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
            val = ds.getValue()
            img = self.snapshot()
            img = column_avg(img)
            # Process sensor data here.
            
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
controller = Marvin()
controller.basic_setup()
controller.continuous_run()
#controller.run()
