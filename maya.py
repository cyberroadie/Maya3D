import sublime, sublime_plugin
from maya_tools import MayaTools

class MayaCommand(sublime_plugin.TextCommand, MayaTools):
    def run(self, edit):
        self.view.run_command("select_all")
        sels = self.view.sel()
        command = self.view.substr(sels[0])
        self.SendCommand(command)
