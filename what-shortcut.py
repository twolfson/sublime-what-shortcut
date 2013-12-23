import glob
import os
import sublime
import sublime_plugin


class WhatShortcutCommand(sublime_plugin.WindowCommand):
    def get_platform_keymaps(self):
        """Collect all .sublime-keymap files for the current platform

        Example: Packages/User/Default (Linux).sublime-keymap
        """
        package_dir = sublime.packages_path()
        platform = sublime.platform().title()
        keymap_glob = os.path.join(package_dir,
                                   '**/Default (%s).sublime-keymap' % platform)
        keymaps = glob.glob(keymap_glob)
        return keymaps

    def run(self):
        """Be awesome to each other."""
        # view = self.window.active_view()
        print self.get_platform_keymaps()
