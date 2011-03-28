"""
    Phidgets-Eventor-Tx
                
    Created on 2010-10-21
    @author: jldupont
"""
import os
import sys

PKG_NAME="phidgets-eventor"
APP_NAME="Phidgets Eventor"
ICON_NAME="phidgets-eventor.png"
HELP_URL="http://www.systemical.com/doc/opensource/phidgets-eventor"
TIME_BASE=5000

###<<< DEVELOPMENT MODE SWITCHES
MSWITCH_OBSERVE_MODE=False
MSWITCH_DEBUGGING_MODE=False
MSWITCH_DEBUG_INTEREST=False
DEV_MODE=True
###>>>

if os.environ.get("JLD_DEV"):
    print "> DEV MODE"
    this_dir=os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(this_dir, PKG_NAME))
else:
    ## make sure to synchronize this with makefile
    sys.path.insert(0, "/usr/share/%s" % PKG_NAME)


import gobject, dbus.glib, gtk
from dbus.mainloop.glib import DBusGMainLoop

gobject.threads_init()  #@UndefinedVariable
dbus.glib.init_threads()
DBusGMainLoop(set_as_default=True)

from phidgets_eventor.system import base as base
base.debug=DEV_MODE
base.debug_interest=MSWITCH_DEBUG_INTEREST

from phidgets_eventor.system import mswitch #@UnusedImport
mswitch.observe_mode=MSWITCH_OBSERVE_MODE
mswitch.debugging_mode=MSWITCH_DEBUGGING_MODE

from phidgets_eventor.agents.notifier import notify

def main(debug=False):
    try:
        
        import phidgets_eventor.agents.adbus
        
        from phidgets_eventor.res import get_res_path
        icon_path=get_res_path()
        
        from phidgets_eventor.agents.phidgets_eventor_tray import TrayAgent
        _ta=TrayAgent(APP_NAME, icon_path, ICON_NAME, HELP_URL)

        import phidgets_eventor.agents.adbus #@UnusedImport

        from phidgets_eventor.agents.notifier import NotifierAgent #@Reimport
        _na=NotifierAgent(APP_NAME, ICON_NAME)
        _na.start()
        
        clk=Clock(TIME_BASE)
        gobject.timeout_add(TIME_BASE, clk.tick)

        from phidgets_eventor.agents.clock import Clock #@Reimport
        import phidgets_eventor.agents.transmitter  #@UnusedImport
        
        mswitch.publish("__main__", "debug", debug)
        
        gtk.main()
    except KeyboardInterrupt:
        mswitch.quit()
        sys.exit(1)        
        
    except Exception,e:
        notify(APP_NAME, "There was an error: %s" % e)
        mswitch.quit()
        sys.exit(1)

if __name__=="__main__":
    main()

