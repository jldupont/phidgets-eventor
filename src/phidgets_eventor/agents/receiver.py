'''
Created on 2011-03-28

@author: jldupont
'''
import json
from phidgets_eventor.system.base import AgentThreadedBase

class Receiver(AgentThreadedBase):
    
    """{
         "type":   "phidgets-ifk"
        ,"kind":   %s  ## din, dout, ain
        ,"serial": %s
        ,"pin":    %s
        ,"value":  %s
    };"""
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        
    def h_msg(self, info_json):
        #print "h_msg: info_json: %s" % info_json
        try:    info=json.loads(info_json)
        except Exception,e:
            print e
            return
        
        #print "h_msg: %s" % info
        
        try:    type=info["type"].lower()
        except: type=None
        
        if type != "phidgets-ifk":
            return
        
        try:    kind=info["kind"]
        except: kind=None
        
        try:    serial=info["serial"]
        except: serial=None
        
        try:    pin=info["pin"]
        except: pin=None
        
        try:    value=info["value"]
        except: value=None
        
        #print "Receiver: kind(%s) serial(%s) pin(%s) value(%s)" % (kind, serial, pin, value)
                
        self.pub(kind, serial, pin, value)
        

_=Receiver()
_.start()

        