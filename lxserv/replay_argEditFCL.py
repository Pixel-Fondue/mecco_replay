# python

import lx, modo, replay

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""


class CommandClass(replay.commander.CommanderClass):
    """Inserts a comment-only command object into the `Macro().commands` list."""

    def commander_arguments(self):
        return [
            {
                'name': 'query',
                'datatype': 'string',
                'values_list_type': 'fcl',
                'values_list': self.list_commands,
                'flags': ['query']
            }, {
                'name': 'asString',
                'label': "As String",
                'datatype': 'boolean',
                'default': 'false',
                'flags': ['optional']
            }
        ]

    def commander_notifiers(self):
        return [("replay.notifier", "")]

    def remove_duplicates(self, seq):
        """Removes duplicate list items while maintaining list order."""
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

    def list_commands(self):
        nodes = replay.Macro().selected_commands
        
        asString = self.commander_args().get('asString', False)

        # Collect args of selected commands
        args = []
        for node in nodes:
            command_obj = node.attributes()
            for arg in node.args:
                if not command_obj.arg(arg.index).is_hidden(True):
                    args.append(arg.argName)
                    
        # Collect selected args
        for arg in replay.Macro().selected_args:
            command_obj = arg.parent.attributes()
            if not command_obj.arg(arg.index).is_hidden(True):
                args.append(arg.argName)

        commands_list = []
        for arg in self.remove_duplicates(args):
            commands_list.append('replay.argEdit%s %s ?' % ("AsString" if asString else "", arg))

        return commands_list                

lx.bless(CommandClass, 'replay.argEditFCL')
