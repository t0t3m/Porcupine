# Porcupine:

Software to prevent unauthorized physical access to your machine.<br>
It listens for udev events and could take 3 different actions when certain storage devices are detected:<br>
  1. Defense (Reboot PC)<br>
  2. Offense (If it's a USB drive, it'll be overwritten, if it's a CD/DVD ROM it'll be eject)<br>
  3. Offense + Defense (The previus modes, combined)<br>

I suggest you (it's quite a must...) to use Full Disk Encryption in order to obtain the best results<br>
(e.g. What happens if someone try to stick his USB pendrive in your PC? In defensive mode, the PC will reboot and<br> 
the intruder will be redirected to FDE password prompt)<br>

This program is created with int0x80 talk "Ant-Forensic for the Louise" from Derbycon 2012 in mind.<br>
For every reference about the original concept by int0x80 please look at:<br>
- GitHub  - https://github.com/int0x80/anti-forensics<br>
- Youtube - "Anti-Forensic for the Louise" http://www.youtube.com/watch?v=-HK1JHR7LIM<br>
- Youtube - "Moar Anti-Forensic for the Louise" http://www.youtube.com/watch?v=i3nLrJrkYOc<br>


# Requirements:

**Must:**<br>
- A PC with a Linux distribution installed (preferred: Ubuntu, Mint)<br>
- Python interpreter, pyudev library and wxwidget bindings for python.<br>
  - python >= 2.7<br>
  - python-wxgtk2.8 >= 2.8.12.1<br>
  - pyudev >= 0.16.1<br>
    e.g. On Ubuntu 11.04: sudo apt-get install python-wxgtk2.8 python<br>
         About pyudev >= 0.16.1 on ubuntu systems  look at:<br>
         https://launchpad.net/ubuntu/raring/i386/python-pyudev/0.16.1-1<br>

**Should:**<br>
- HD with Full Disk Encryption enabled e with a sifficient strong password


# Usage:

Simply run it with superadmin privileges<br>


# ToDo:

- Add MMC/SD/others controls<br>
- Add a checksum system for personal pendrives<br>
- Add the options to run default actions when device is detected<br>
- Add Shortcut and menu option to hide the trayicon (partially implemented. At the moment<br>
  only hide is possible, no resume from hide)<br>
- Password protect Quit action (maybe)<br>
- Password protect Settings menu (maybe)<br>
- Password protect Stop action (maybe)<br>
- Password protect Show trayicon action (maybe)<br>
- Fill or remove the about messagebox<br>
- Fix tray icon<br>
- Clean and revise code<br>
- More Tests<br>


# Known bugs:

- Sometimes the tray icon is displayed wrong<br>
