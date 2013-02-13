import os
import pickle
import wx

DEVICES_FILE = "./configs/devices.conf"
FILES_FILE = "./configs/files.conf"

class ListUtils:
    ''' Load a file into a list '''
    def LoadFromFile(self, load_file):
        if(os.path.isfile(load_file) == True):
            f = open(load_file, 'rb')
            lst = pickle.load(f)
            f.close()
            return lst
        else:
            f = open(load_file, 'wb')
            lst = []
            pickle.dump(lst, f)
            f.close()
            return lst
    
    ''' Save a list into a file '''
    def SaveToFile(self, lst, save_file):
        if(os.path.isfile(save_file) == True):
            f = open(save_file, 'wb')
            pickle.dump(lst, f)
            f.close()
        else:
            f = open(save_file, 'wb')
            pickle.dump(lst, f)
            f.close()

    ''' Update listctrl from a list '''
    def ListctrlUpdate(self, lstctrl, lst, fil):
        lstctrl.DeleteAllItems()
        res = self.LoadFromFile(fil)
        for item in res:
            lstctrl.Append(item)

    ''' Delete an item from the listctrl and the corresponding list '''
    def DelItem(self, lst, lstctrl, fil):
        item = lstctrl.GetFirstSelected()        
        for items in lst:
            res = lstctrl.GetItemText(item)
            if items[0] == res:
                del lst[item]
            else:
                pass
        lstctrl.DeleteItem(item)
        self.SaveToFile(lst, fil)
        self.ListctrlUpdate(lstctrl, lst, fil)

    ''' find an item in a list '''
    def FindItem(self, lst, data):

        for item in lst:
            if data in item:
                return True

        return False

class DevicesList(ListUtils):
    def AddDevice(self, lst, dev_type, serial):
        lst.append((dev_type, serial))
        self.SaveToFile(lst, DEVICES_FILE)

    def ListctrlToList(self, lstctrl, lst):
        count = lstctrl.GetItemCount()
        items = []
        for item in range(count):
            items.append((lstctrl.GetItem(item, 0).GetText(),
                          lstctrl.GetItem(item, 1).GetText()
                        ))
        return items

class FilesList(ListUtils):
    def AddFile(self, lst, file_picker):
        lst.append((file_picker.GetPath(),0))
        self.SaveToFile(lst, FILES_FILE)

    def ListctrlToList(self, lstctrl, lst):
        count = lstctrl.GetItemCount()
        items = []
        for item in range(count):
            items.append((lstctrl.GetItem(item, 0).GetText(), 0))
        return items