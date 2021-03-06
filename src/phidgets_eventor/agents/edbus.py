"""
    Phidgets-Eventor Dbus Agent
    
    Created on 2010-10-22
    @author: jldupont
    
"""
import dbus.service
    
from phidgets_eventor.system.base import AgentThreadedBase
from phidgets_eventor.system import mswitch

__all__=[]

class SignalHandlerEventor(dbus.service.Object):
    PATH="/Events"
    IFACE="com.systemical.eventor"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SystemBus(), self.PATH)
        
        dbus.SystemBus().add_signal_receiver(self.sMsg,
                                       signal_name="Msg",
                                       dbus_interface=self.IFACE,
                                       bus_name=None,
                                       path=self.PATH
                                       )            
        #print "edbus.SignalHandlerEventor"

    def sMsg(self, info_json):
        #print "SignalHandlerEventor: %s" % p
        #print "SignalHandlerEventor: info_json: %s" % info_json
        mswitch.publish("__edbus__", "msg", info_json)

_sh=SignalHandlerEventor()


class SignalTxSensors(dbus.service.Object):
    """
    DBus signals handler
    """
    PATH    = "/State"
    BUS_NAME= "org.sensors"
    INTERF  = "org.sensors"
    
    def __init__(self):
        self.bus=dbus.SessionBus()
        bus_name = dbus.service.BusName(self.BUS_NAME, self.bus)
        dbus.service.Object.__init__(self, bus_name, self.PATH)
        
    @dbus.service.signal(dbus_interface="org.sensors", signature="ssv")
    def State(self, device_id, sensor_name, sensor_state):
        """Generated when a sensor changes state"""
    

class SignalTxPhidgets(dbus.service.Object):
    
    PATH="/Device"
    IFACE="com.phidgets.Phidgets"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SystemBus(), self.PATH)        

    @dbus.service.signal(dbus_interface=IFACE, signature="sii")        
    def Din(self, serial, pin, value):
        """Generated to report state of a digital input"""
    
    @dbus.service.signal(dbus_interface=IFACE, signature="sii")
    def Dout(self, serial, pin, value):
        """Generated to report state of a digital output"""

    @dbus.service.signal(dbus_interface=IFACE, signature="sii")
    def Ain(self, serial, pin, value):
        """Generated to report state of a analog input"""
        
    @dbus.service.signal(dbus_interface=IFACE, signature="sii")
    def State(self, serial, pin, value):
        """Generated to report state of a analog input"""


class SignalTxAgent(AgentThreadedBase):
    def __init__(self):
        AgentThreadedBase.__init__(self)
        self.tx=SignalTxPhidgets()
        self.txSensors=SignalTxSensors()
        
        
    def h_din(self, serial, pin, value):
        self.tx.Din(serial, pin, value)
        
    def h_dout(self, serial, pin, value):
        self.tx.Dout(serial, pin, value)
        
    def h_ain(self, serial, pin, value):
        self.tx.Ain(serial, pin, value)

    def h_changed(self, kind, serial, pin, value):
        self.txSensors.State(serial, "%s:%s" % (kind, pin), value)
        

_stx=SignalTxAgent()
_stx.start()
   

