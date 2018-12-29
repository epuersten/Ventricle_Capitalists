# Ventricle_Capitalists
Code repository for all project information relating to 3K04 Software Design (Pacemaker)

Simulink files require Matlab Simulink to open.
If you are on the School Network you must use a VM (VMWare Horizon Client). If you are not on the school network you must use VPN (Cisco VPN) and a VM. 

Required python modules to run the DCM:
matplotlib
pySerial

These can be installed by running in command prompt
python -m pip install matplotlib
python -m pip install pySerial

BASIC SERIAL TESTING
Basic Serial tests are run via SerialTest.py
This requires you to also have:
(1) _SerialHandler.py
(2) installed pySerial

DCM TESTING:
DCM test are run via DCMLaunch.py
This requires you to also have:
(1) _SerialHandler.py
(2) _PopupWindow.py
(3) _EgramWindow.py
(4) _LoginWindow.py
(5) _HomeWindow.py
(6) installed pySerial and installed matplotlib
