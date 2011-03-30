'''
Created on 2011-03-29

@author: jldupont
'''
from phidgets_eventor.system.base import AgentThreadedBase

class Debouncer(AgentThreadedBase):
    
    def __init__(self):
        AgentThreadedBase.__init__(self)

        self.map={}
    
    def h_din(self, serial, pin, value):
        self._process("din", serial, pin, value)
    
    def h_dout(self, serial, pin, value):
        self._process("dout", serial, pin, value)
    
    def h_ain(self, serial, pin, value):
        self._process("ain", serial, pin, value)
    
    def _process(self, kind, serial, pin, value):
        key="%s:%s:%s" % (kind, serial, pin)
        previous_value=self.map.get(key, None)
        if value != previous_value:
            self.map[key]=value
            self.pub("changed", kind, serial, pin, value)
    

_=Debouncer()
_.start()
