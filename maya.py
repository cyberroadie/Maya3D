import sublime, sublime_plugin
from maya_tools import MayaTools

class MayaCommand(sublime_plugin.TextCommand, MayaTools):
    def run(self, edit):
        if len(self.view.sel()[0]) == 0:
            self.view.run_command("select_all")
        sels = self.view.sel()
        for sel in sels:
            command = self.view.substr(sel)
            self.SendCommand(command)
