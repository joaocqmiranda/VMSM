import os
import Init
import FreeCADGui
from VMSM import

path_scaleWB = os.path.dirname(Init.__file__)
path_scaleWB_icons =  os.path.join( path_scaleWB, 'resources')

global main_ScaleWB_Icon
main_ScaleWB_Icon = os.path.join( path_scaleWB_icons , 'convert.svg')

class MyCommand2():


    def GetResources(self):
        return {'Pixmap'  : main_ScaleWB_Icon, # the name of a svg file available in the resources
                #'Accel' : "Shift+S", # a default shortcut (optional)
                'MenuText': "My New Command",
                'ToolTip' : "What my new command does"}

    def Activated(self):

        return

    def IsActive(self):

        return True


FreeCADGui.addCommand('MyCommand2',MyCommand2())