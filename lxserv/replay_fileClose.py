import lx, modo, replay

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""


class CommandClass(replay.commander.CommanderClass):

    """Close the current `Macro()` and, if necessary, prompt user to save changes."""
    def commander_execute(self, msg, flags):

        macro = replay.Macro()
        # If content is not empty ask user for save
        if not macro.is_empty:
            file_path = macro.file_path
            if file_path is None:
                file_path = "Untitled"
            if modo.dialogs.yesNo("Save changes", "Do you want to save changes in \'" + file_path + "'") == 'yes':
                # If file path is not assigned ask for new file path
                if macro.file_path is None:
                    file_path = modo.dialogs.customFile(dtype = 'fileSave', title = 'Save LXM file', \
                                                 names = ('LXM',), unames = ('LXM file'), ext=('LXM',))
                macro.render_LXM(file_path)
        # Clear current macro
        macro.clear()
        macro.rebuild_view()

lx.bless(CommandClass, 'replay.fileClose')
