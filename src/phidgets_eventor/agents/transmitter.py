'''
Created on 2011-03-28

@author: jldupont
'''
from phidgets_eventor.system.base import AgentThreadedBase
from phidgets_eventor.system.network import MulticastTransmitter

class Transmitter(AgentThreadedBase):
    
    GROUP = "239.0.0.1"
    PORT  = 6666

    TPL="""{
         "type":   "phidgets-ifk"
        ,"kind":   %s
        ,"serial": %s
        ,"pin":    %s
        ,"value":  %s
    };"""
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        
        self.mt=MulticastTransmitter(self.GROUP, self.PORT)
        
    def h_sensor(self, type, serial, pin, value):
        """
        """
        s=self.TPL % (type, serial, pin, value)
        self.mt.send(s)


_=Transmitter()
_.start()

        