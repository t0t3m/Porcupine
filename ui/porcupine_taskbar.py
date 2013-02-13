import wx
from wx import xrc


class PorcupineTaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon('icons/porcupine_icon.png', wx.BITMAP_TYPE_PNG), 'Porcupine')
        self.Bind(wx.EVT_MENU, self.frame.ObserverStart, id=1)
        self.Bind(wx.EVT_MENU, self.frame.ObserverStop, id=2)
        self.Bind(wx.EVT_MENU, self.frame.PorcupineSettings, id=3)
        self.Bind(wx.EVT_MENU, self.frame.PorcupineTaskbarHide, id=4)
        self.Bind(wx.EVT_MENU, self.frame.PorcupineQuit, id=5)

    def CreatePopupMenu(self):
        self.menu = wx.Menu()
        self.menu.Append(1, 'Start')
        self.menu.Append(2, 'Stop')
        self.menu.Append(3, 'Settings')
        self.menu.Append(4, 'Hide')
        self.menu.Append(5, 'Quit')
        return self.menu