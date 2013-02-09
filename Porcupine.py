#!/usr/bin/python

import wx
from wx import xrc
import lib.observer


class Porcupine_main(wx.Frame):
    def __init__(self):
        self.InitUI()
        self.observer_status = 0
        self.obs = lib.observer.Observer(self.radio_mode, self.chkbox_usb, self.chkbox_cd, self.chkbox_sd, self.chkbox_dmesg, self.chkbox_bash_history)
        self.tskic = PorcupineTaskBarIcon(self)

    def InitUI(self):
        self.ui = xrc.XmlResource('Porcupine.xrc')
        self.frame_settings = self.ui.LoadFrame(None, 'Porcupine_settings')
        
        self.radio_mode = xrc.XRCCTRL(self.frame_settings, "radiobox_mode")
        self.chkbox_usb = xrc.XRCCTRL(self.frame_settings, "chkbox_usb")
        self.chkbox_cd = xrc.XRCCTRL(self.frame_settings, "chkbox_cd")
        self.chkbox_sd = xrc.XRCCTRL(self.frame_settings, "chkbox_sd")
        self.chkbox_dmesg = xrc.XRCCTRL(self.frame_settings, "chkbox_dmesg")
        self.chkbox_bash_history = xrc.XRCCTRL(self.frame_settings, "chkbox_bash_history")
        self.frame_settings.Bind(wx.EVT_CLOSE, self.FrameClose)

    def OnHide(self, event):
        self.tskic.RemoveIcon()

    def Quit(self, event):
        self.tskic.Destroy()
        if self.frame_settings:
            self.frame_settings.Destroy()

    def FrameClose(self, event):
        self.frame_settings.Hide()

    def Settings(self, event):
        if not self.frame_settings:
            self.frame_settings = self.ui.LoadFrame(None, 'Porcupine_settings')
        self.frame_settings.Show()

    def ObserverStart(self, event):
    	if(self.observer_status == 0):
            self.obs.Start()
            self.observer_status = 1
        elif(self.observer_status == 1):
            pass
        else:
            pass

    def ObserverStop(self, event):
        if(self.observer_status == 1):
            self.obs.Stop()
            self.observer_status = 0
        elif(self.observer_status == 0):
            pass
        else:
            pass


class PorcupineTaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon('porcupine_icon.png', wx.BITMAP_TYPE_PNG), 'Porcupine')
        self.Bind(wx.EVT_MENU, self.frame.ObserverStart, id=1)
        self.Bind(wx.EVT_MENU, self.frame.ObserverStop, id=2)
        self.Bind(wx.EVT_MENU, self.frame.Settings, id=3)
        self.Bind(wx.EVT_MENU, self.frame.OnHide, id=4)
        self.Bind(wx.EVT_MENU, self.frame.Quit, id=5)

    def CreatePopupMenu(self):
        self.menu = wx.Menu()
        self.menu.Append(1, 'Start')
        self.menu.Append(2, 'Stop')
        self.menu.Append(3, 'Settings')
        self.menu.Append(4, 'Hide')
        self.menu.Append(5, 'Quit')
        return self.menu


class Porcupine_app(wx.App):
    def OnInit(self):
        Porcupine_main()
        return True

app = Porcupine_app(0)
app.MainLoop()