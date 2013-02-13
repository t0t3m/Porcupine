import subprocess
import wx
from wx import xrc
import porcupine_taskbar
import os

import lib.observer
import lib.listutils as listutils

DEVICES_FILE = "./configs/devices.conf"
FILES_FILE = "./configs/files.conf"

class Porcupine_UI(wx.Frame):
    def __init__(self):
        if(os.getuid() == 0):
            # Init UI
            self.InitUI()

            # Setup devices lists
            self.dev_lst = listutils.DevicesList()
            self.devices_list = self.dev_lst.LoadFromFile(DEVICES_FILE)
            self.dev_lst.ListctrlUpdate(self.lstctrl_devices, self.devices_list, DEVICES_FILE)

            # Setup files lists
            self.files_lst = listutils.FilesList()
            self.files_list = self.files_lst.LoadFromFile(FILES_FILE)
            self.files_lst.ListctrlUpdate(self.lstctrl_files, self.files_list, FILES_FILE)

            # Init TaskBarIcon
            self.tskic = porcupine_taskbar.PorcupineTaskBarIcon(self)

            # Init Observer
            self.observer_status = 0
            self.obs = lib.observer.Observer(self.radio_mode, self.chkbox_usb, self.chkbox_cd, self.chkbox_sd, self.dev_lst, self.devices_list, self.lstctrl_devices, self.files_list)
        else:
            wx.MessageDialog(None, "Please run with administrator privileges.", 'Error', wx.OK|wx.ICON_WARNING).ShowModal()

    ''' Hide porcupine taskbar icon '''
    def PorcupineTaskbarHide(self, event):
        self.tskic.RemoveIcon()
    
    ''' Quit porcupine '''
    def PorcupineQuit(self, event):
        self.tskic.Destroy()
        if self.frame_porcupine:
            self.frame_porcupine.Destroy()

    ''' Hide Porcupine taskbar icon '''
    def PorcupineFrameClose(self, event):
        self.frame_porcupine.Hide()

    ''' Show Porcupine setting frame from taskbar icon'''
    def PorcupineSettings(self, event):
        if not self.frame_porcupine:
            self.frame_porcupine = self.ui.LoadFrame(None, 'Porcupine_settings')
        self.frame_porcupine.Show()

    ''' Start the udev observer '''
    def ObserverStart(self, event):
        if(self.observer_status == 0):
            self.obs.Start()
            self.observer_status = 1
        elif(self.observer_status == 1):
            pass
        else:
            pass

    ''' Stop the udev observer '''
    def ObserverStop(self, event):
        if(self.observer_status == 1):
            self.obs.Stop()
            self.observer_status = 0
        elif(self.observer_status == 0):
            pass
        else:
            pass

    ''' Initialize user interface widgets and stores them '''
    def InitUI(self):
        # Load XRC file, initialize frame and bind close action to frame
        self.PorcupineFrameInit()
        # Init UI tabs and sections
        self.PorcupineSettingsTab()
        self.TrustedDevicesTab()
        self.EmergencyWipeTab()
    
    ''' Init Porcupine frame from XRC file '''
    def PorcupineFrameInit(self):
        # Load XRC file, initialize frame and bind close action to frame 
        self.ui = xrc.XmlResource('ui/Porcupine.xrc')
        self.frame_porcupine = self.ui.LoadFrame(None, 'Porcupine_settings')
        self.frame_porcupine.Bind(wx.EVT_CLOSE, self.PorcupineFrameClose)

    ''' Init Porcupine Settings tab '''
    def PorcupineSettingsTab(self):
        # Porcupine settings widgets 
        self.radio_mode = xrc.XRCCTRL(self.frame_porcupine, "radiobox_mode")
        self.chkbox_usb = xrc.XRCCTRL(self.frame_porcupine, "chkbox_usb")
        self.chkbox_cd = xrc.XRCCTRL(self.frame_porcupine, "chkbox_cd")
        self.chkbox_sd = xrc.XRCCTRL(self.frame_porcupine, "chkbox_sd")

    ''' Init Trusted devices tab '''
    def TrustedDevicesTab(self):
        # Porcupine trusted devices widgets
        self.lstctrl_devices = xrc.XRCCTRL(self.frame_porcupine, "lst_trusted_devices")
        self.btn_refresh_devices = xrc.XRCCTRL(self.frame_porcupine, "btn_refresh_devices")
        self.btn_delete_device = xrc.XRCCTRL(self.frame_porcupine, "btn_delete_device")
        self.btn_refresh_devices.Bind(wx.EVT_BUTTON, self.RefreshDevices)
        self.btn_delete_device.Bind(wx.EVT_BUTTON, self.DeleteDevice)
        self.lstctrl_devices.InsertColumn(0, 'Serial')
        self.lstctrl_devices.InsertColumn(1, 'Type')

    ''' Init emergency wipe tab '''
    def EmergencyWipeTab(self):
        # Porcupine wipe tab widgets
        self.lstctrl_files = xrc.XRCCTRL(self.frame_porcupine, "lstctrl_files")
        self.picker_file = xrc.XRCCTRL(self.frame_porcupine, "picker_file")
        self.btn_add_file = xrc.XRCCTRL(self.frame_porcupine, "btn_add_file")
        self.btn_del_file = xrc.XRCCTRL(self.frame_porcupine, "btn_del_file")
        self.btn_refresh_files = xrc.XRCCTRL(self.frame_porcupine, "btn_refresh_files")
        self.lstctrl_files.InsertColumn(0, 'File')
        self.btn_add_file.Bind(wx.EVT_BUTTON, self.AddFile)
        self.btn_del_file.Bind(wx.EVT_BUTTON, self.DeleteFile)
        self.btn_refresh_files.Bind(wx.EVT_BUTTON, self.RefreshFiles)

    ''' Action on Refresh devices button clicked '''
    def RefreshDevices(self, event):
        self.dev_lst.ListctrlUpdate(self.lstctrl_devices, self.devices_list, DEVICES_FILE)

    ''' Action on Delete device button clicked '''
    def DeleteDevice(self, event):
        self.dev_lst.DelItem(self.devices_list, self.lstctrl_devices, DEVICES_FILE)

    ''' Action on Refresh files button clicked '''
    def RefreshFiles(self, event):
        self.files_lst.ListctrlUpdate(self.lstctrl_files, self.files_list, FILES_FILE)

    ''' Action on Delete files button clicked '''
    def DeleteFile(self, event):
        self.files_lst.DelItem(self.files_list, self.lstctrl_files, FILES_FILE)

    ''' Action on Add file button clicked '''
    def AddFile(self, event):
        self.files_lst.AddFile(self.files_list, self.picker_file)
        self.files_lst.ListctrlUpdate(self.lstctrl_files, self.files_list, FILES_FILE)