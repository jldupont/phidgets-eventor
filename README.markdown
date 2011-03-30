This project consists of a multicast event bridge ("Eventor") to Phidgets-DBus. 

Applications
------------

 - "phidgets-eventor-tx" : transmitter
   Phidgets related DBus signals are sent as per "Eventor" multicast bridging specification.

 - phidgets-eventor-rx : receiver of "Eventor" DBus signals, translation to local Phidgets-DBus signals

Installation
============
There are 2 methods:

1. Use the Ubuntu Debian repository [jldupont](https://launchpad.net/~jldupont/+archive/jldupont)  with the package "phidgets-eventor"

2. Use the "Download Source" function of this git repo and use "sudo make install"

Dependencies
============

* DBus python bindings

History
=======

 - v1.0 : initial release 

 - v1.1 : with phidgets-eventor-rx
