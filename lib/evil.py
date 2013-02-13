import subprocess
import os

import threading
from multiprocessing import Pool

class Evil:
    ''' Reboot PC '''
    def Reboot(self):
        subprocess.call("reboot", shell = True)

    ''' Simulate fork bomb to freeze PC and overwrite all RAM'''
    def SimForkBomb(self):
        while True:
            os.fork()

    ''' Overwrite an intruder device '''
    def Overwrite(self, device):
        dev = str(device.device_node)
        subprocess.call("cat /dev/urandom > " + dev, shell = True)

    ''' Eject an intruder device '''
    def Eject(self, device):
        dev = str(device.device_node)
        subprocess.call("eject -v " + dev, shell = True)

    '''
    def ThreadedForkBomb(self):
        threading.Thread(target = self.SimForkBomb).start()
        threading.Thread(target = self.SimForkBomb).start()
    '''