import sublime
import sublime_plugin
import subprocess
import re
import os

class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        settings = sublime.load_settings('CommandOnSave.sublime-settings').get('commands')
        touchfile = sublime.load_settings('CommandOnSave.sublime-settings').get('touchfile') or "inhibit-cos"
        file = view.file_name()
        basename = os.path.basename(file)
        dirname = os.path.dirname(file)


        if not (
            settings == None
            or os.path.isfile(os.path.join(dirname,touchfile))
            or os.path.isfile(os.path.expanduser("~/"+touchfile))
        ):
            for path in settings.keys():
                commands = settings.get(path)
                if re.search(path, file) is not None and len(commands) > 0:
                    for command in commands:
                        command = command.format(filename=file,basename=basename,dirname=dirname)
                        print("Command on Save: " + command )
                        p = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
                        out, err = p.communicate()
                        print (out.decode('utf-8'))
