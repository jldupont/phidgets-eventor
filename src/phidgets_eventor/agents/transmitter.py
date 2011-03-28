'''
Created on 2011-03-28

@author: jldupont
'''
from phidgets_eventor.system.base import AgentThreadedBase
from phidgets_eventor.system.network import MulticastTransmitter

class Transmitter(AgentThreadedBase):
    
    GROUP = "239.0.0.1"
    PORT  = 6666
    COUNT = 10
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        
        self.mr=MulticastTransmitter(self.GROUP, self.PORT)
        
    def h_sensor(self, serial, pin, value):
        """
        """



_=Transmitter()
_.start()

        