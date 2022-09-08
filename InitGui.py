import os
import Init

path_scaleWB = os.path.dirname(Init.__file__)
path_scaleWB_icons =  os.path.join( path_scaleWB, 'Resources')

global main_ScaleWB_Icon
main_ScaleWB_Icon = os.path.join( path_scaleWB_icons , 'VMSM.svg')

class MyWorkbench(Workbench):
    MenuText = "VMSM"
    ToolTip = "Visualazation of mechanical systems motion"
    Icon = main_ScaleWB_Icon

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import MyCommand1 #, MyCommand2  # import here all the needed files that create your FreeCAD commands
        self.list = ["MyCommand1"]  # A list of command names created in the line above
        self.appendToolbar("My Commands", self.list)  # creates a new toolbar with your commands
        #self.appendMenu("My New Menu", self.list)  # creates a new menu
        #self.appendMenu(["An existing Menu", "My submenu"], self.list)  # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed when the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list)  # add commands to the context menu

    def GetClassName(self):
        # This function is mandatory if this is a full python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"


Gui.addWorkbench(MyWorkbench())