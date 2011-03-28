"""
    Phidgets-Eventor Dbus Agent
    
    Created on 2010-10-22
    @author: jldupont
    
"""
import dbus.service
    
#from phidgets_eventor.system.base import AgentThreadedBase
from phidgets_eventor.system import mswitch

__all__=[]

class SignalRx(dbus.service.Object):
    PATH="/Device"
    IFACE="com.phidgets.Phidgets"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SessionBus(), self.PATH)
        
        dbus.Bus().add_signal_receiver(self.sDin,
                                       signal_name="Din",
                                       dbus_interface=self.IFACE,
                                       bus_name=None,
                                       path="/Device"
                                       )            

        dbus.Bus().add_signal_receiver(self.sDout,
                                       signal_name="Dout",
                                       dbus_interface=self.IFACE,
                                       bus_name=None,
                                       path="/Device"
                                       )            

        dbus.Bus().add_signal_receiver(self.sAin,
                                       signal_name="Ain",
                                       dbus_interface=self.IFACE,
                                       bus_name=None,
                                       path="/Device"
                                       )            

    def sDin(self, serial, pin, value):
        self._pub("din", serial, pin, value)

    def sDout(self, serial, pin, value):
        self._pub("dout", serial, pin, value)
        
    def sAin(self, serial, pin, value):
        self._pub("ain", serial, pin, value)
        
    def _pub(self, type, serial, pin, value):
        try:
            mswitch.publish(self.__class__, "sensor", type, str(serial), int(pin), int(value))
            #print("Sensor: type(%s) serial(%s) pin(%s) value(%s)" % (type, serial, pin, value))
        except Exception,e:
            print "!!! Signal-RX: exception: %s" % e



_=SignalRx()

