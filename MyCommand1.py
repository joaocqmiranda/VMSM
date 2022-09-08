import os
import Init
import FreeCADGui

path_scaleWB = os.path.dirname(Init.__file__)
path_scaleWB_icons =  os.path.join( path_scaleWB, 'resources')

global main_ScaleWB_Icon
main_ScaleWB_Icon = os.path.join( path_scaleWB_icons , 'convert.svg')

class MyCommand1():


    def GetResources(self):
        return {'Pixmap'  : main_ScaleWB_Icon, # the name of a svg file available in the resources
                #'Accel' : "Shift+S", # a default shortcut (optional)
                'MenuText': "My New Command",
                'ToolTip' : "What my new command does"}

    def Activated(self):
        os.startfile(path_scaleWB + '\\resources\VMSM\dist\VMSM.exe')
        return

    def IsActive(self):

        return True


FreeCADGui.addCommand('MyCommand1',MyCommand1())