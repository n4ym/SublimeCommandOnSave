import sublime
import sublime_plugin
import subprocess


class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        settings = sublime.load_settings('CommandOnSave.sublime-settings').get('commands')
        file = view.file_name()

        if not settings == None:
            for path in settings.keys():
                commands = settings.get(path)
                if re.match(path, file) is not None and len(commands) > 0:
                    print("Command on Save:")
                    for command in commands:
                        command = command.format(filename=file)
                        p = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
                        out, err = p.communicate()
                        print (out.decode('utf-8'))
