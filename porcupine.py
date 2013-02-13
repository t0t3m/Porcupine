#!/usr/bin/python

import wx
from wx import xrc
import ui.porcupine_ui

class Porcupine_app(wx.App):
    def OnInit(self):
        ui.porcupine_ui.Porcupine_UI()
        return True

app = Porcupine_app(0)
app.MainLoop()