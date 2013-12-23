import sublime_plugin


class WhatShortcutCommand(sublime_plugin.WindowCommand):
    def run(self):
        """Be awesome to each other."""
        view = self.window.active_view()
        print view.settings().__dict__
