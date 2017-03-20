import lx, modo, replay
from replay import message as message

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""


class CommandClass(replay.commander.CommanderClass):

    """Close the current `Macro()` and, if necessary, prompt user to save changes."""
    def commander_execute(self, msg, flags):

        macro = replay.Macro()

        # Hack to fix crash bug.
        macro.select_event_treeview()

        # If content is not empty ask user for save
        if macro.unsaved_changes and not macro.is_empty:
            file_path = macro.file_path
            if file_path is None:
                file_path = "Untitled"
            if modo.dialogs.yesNo(message("MECCO_REPLAY", "ASK_FOR_SAVE_DIALOG_TITLE"), message("MECCO_REPLAY", "ASK_FOR_SAVE_DIALOG_MSG")) == 'yes':
                # If file path is not assigned ask for new file path
                if macro.file_path is None:
                    file_path = modo.dialogs.customFile(dtype = 'fileSave', title = message("MECCO_REPLAY", "SAVE_DIALOG_TITLE"), \
                                                 names = ('LXM',), unames = ('LXM file'), ext=('LXM',))
                macro.render_LXM(file_path)

        # No more file path
        macro.file_path = None
        macro.file_format = None
        macro.unsaved_changes = False
        # Stop recording
        lx.eval('replay.record stop')
        # Clear current macro
        macro.clear()
        # Rebuild treeview
        macro.rebuild_view()

        notifier = replay.Notifier()
        notifier.Notify(lx.symbol.fCMDNOTIFY_CHANGE_ALL)

    def basic_Enable(self, msg):
        return True

lx.bless(CommandClass, 'replay.fileClose')
