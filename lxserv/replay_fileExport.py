import lx, modo, replay_commander, replay

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""

class CommandClass(replay_commander.CommanderClass):
    """Export the current `ReplayMacro()` to LXM, PY, or JSON using its built-in
    export methods. Accepts optional format and destination arguments. If either
    of these is not provided, a `modo.dialogs.customFile()` will be thrown."""

    def commander_arguments(self):
        return [
            {
                'name': 'format',
                'datatype': 'string',
                'default': replay.ReplayMacro().export_formats[0],
                'values_list_type': 'popup',
                'values_list': replay.ReplayMacro().export_formats,
                'flags': ['optional']
            }, {
                'name': 'destination',
                'datatype': 'string',
                'flags': ['optional']
            }
        ]

    def commander_execute(self, msg, flags):

        # see http://modo.sdk.thefoundry.co.uk/td-sdk/dialogs.html#custom-file-dialog
        pass


lx.bless(CommandClass, 'replay.fileExport')
