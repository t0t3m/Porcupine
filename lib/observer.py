import lib.evil
import pyudev.wx
from pyudev import Context, Monitor

class Observer:
    def __init__(self, radio_mode, chkbox_usb, chkbox_cd, chkbox_sd, chkbox_dmesg, chkbox_bash_history, chkbox_general_logs):
        self.context = Context()
        self.evil = lib.evil.Evil(self)
        self.radio_mode = radio_mode
        self.chkbox_usb = chkbox_usb
        self.chkbox_cd = chkbox_cd
        self.chkbox_sd = chkbox_sd
        self.chkbox_dmesg = chkbox_dmesg
        self.chkbox_bash_history = chkbox_bash_history
        self.chkbox_general_logs = chkbox_general_logs

    def Start(self):
        self.monitor = Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='block')
        self.obs = pyudev.wx.WxUDevMonitorObserver(self.monitor)
        self.obs.Bind(pyudev.wx.EVT_DEVICE_EVENT, self.actions_to_take)
        self.monitor.start()

    def Stop(self):
        self.obs.enabled = False

    def actions_to_take(self, event):
        if(self.is_usb(event) == True and self.radio_mode.GetStringSelection() == "Defensive" and self.chkbox_usb.GetValue() == True):
            self.log_actions(self.chkbox_dmesg, self.chkbox_bash_history)
            self.evil.Reboot()
        elif(self.is_usb(event) == True and self.radio_mode.GetStringSelection() == "Offensive" and self.chkbox_usb.GetValue() == True):
            self.evil.Overwrite(event.device)
            self.log_actions(self.chkbox_dmesg, self.chkbox_bash_history)
        elif(self.is_usb(event) == True and self.radio_mode.GetStringSelection() == "Offensive + Defensive" and self.chkbox_usb.GetValue() == True):
            self.evil.Overwrite(event.device)
            self.log_actions(self.chkbox_dmesg, self.chkbox_bash_history)
            self.evil.Reboot()
        elif(self.is_cd(event) == True and self.radio_mode.GetStringSelection() == "Defensive" and self.chkbox_cd.GetValue() == True):
            self.log_actions(self.chkbox_dmesg, self.chkbox_bash_history)
            self.evil.Reboot() 
        elif(self.is_cd(event) == True and self.radio_mode.GetStringSelection() == "Offensive" and self.chkbox_cd.GetValue() == True):
            self.log_actions(self.chkbox_dmesg, self.chkbox_bash_history)
            self.evil.Eject(event.device)
        elif(self.is_cd(event) == True and self.radio_mode.GetStringSelection() == "Offensive + Defensive" and self.chkbox_cd.GetValue() == True):
            self.log_actions(self.chkbox_dmesg, self.chkbox_bash_history)
            self.evil.Eject(event.device)
            self.evil.Reboot()
        else:
            pass

    def is_usb(self, event):
        if(str(event.action) == "add" and str(event.device.device_node[7]) != "a" and str(event.device.device_node[5:7]) == "sd" and event.device['ID_BUS'] != "scsi" and event.device['ID_BUS'] == "usb"):
            return True
        else:
            return False

    def is_cd(self, event):
        if(str(event.action) == "change" and str(event.device.device_node[5:7]) == "sr" and self.chkbox_cd.GetValue() == True and event.device['ID_BUS'] == "scsi" and event.device['ID_TYPE'] == 'cd'):
            return True
        else:
            return False

    def is_sd(self, event):
        pass

    def log_actions(self, chkbox_dmesg, chkbox_bash_history):
        if(self.chkbox_dmesg.GetValue() == True):
            self.evil.clean_dmesg()
        if(self.chkbox_bash_history.GetValue() == True):
            self.evil.clean_bash_history()
        if(self.chkbox_general_logs.GetValue() == True):
            self.evil.clean_logs()