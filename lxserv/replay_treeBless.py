# python

from replay import Macro


# In order to be available in the GUI, a treeview needs to be "blessed" (same as
# MODO commands.) Lumberjack does all of this automatically with a single
# `bless()` method. It can only be fired once per session.

Macro().bless(

    # :param viewport_type:   category in the MODO UI popup
    #                         vpapplication, vp3DEdit, vptoolbars, vpproperties, vpdataLists,
    #                         vpinfo, vpeditors, vputility, or vpembedded
    viewport_type = 'vputility',

    # :param nice_name:       display name for the treeview in window title bars, etc
    #                         should ideally be a message table lookup '@table@message@'
    nice_name = 'Replay',

    # :param internal_name:   name of the treeview server (also used in config files)
    internal_name = 'replayTreeView',

    # :param ident:           arbitrary unique four-letter all-caps identifier (ID4)
    ident = 'RRTV',

    # :param column_definitions:         a list of dictionaries, one for each column. Values in each
    #                         node's values dictionary must correspond with these strings
    column_definitions = {
        'primary_position': 2,
        'list': [
                {
                    'name':'name',
                    # negative integers are summed and then divided for relative widths.
                    # in this example, -1 + -3 == -4, so -1/-4 is 25%.
                    'width':-1
                }, {
                    'name':'enable',
                    # positive integers are pixel values (i.e. 20px)
                    'width':24,
                    'icon_resource':'uiicon_replay_suppress'
                }, {
                    'name':'prefix',
                    'width':24,
                    'justify':'center',
                    'icon_resource':'uiicon_replay_prefix'
                }, {
                    'name':'command',
                    'width':-1
                }
            ]
    },

    # :param input_regions:   list of regions for input remapping. These can be implemented from
    #                         within the data object itself as described in TreeData(), and used
    #                         in InputRemapping config files, like this:
    #
    #                         <atom type="InputRemapping">
    #                             <hash type="Region" key="treeViewConfigName+(contextless)/(stateless)+regionName@rmb">render</hash>
    #                         </atom>
    #
    #                         NOTE: slot zero [0] in the list is reserved for the .anywhere region.
    #                         Don't use it.
    #
    #                         [
    #                             '(anywhere)',       # 0 reserved for .anywhere
    #                             'regionNameOne',    # 1
    #                             'regionNameTwo'     # 2
    #                         ]

    input_regions = [
        '(anywhere)', # 0 is reserved ".anywhere" region index
        'MacroCommandCommand',
        'MacroCommandArg',
        'MacroCommandEnable',
        'MacroCommandPrefix',
        'MacroCommandBlock'
    ],

    # :param notifiers:       Returns a list of notifier tuples for auto-updating the tree. Optional.
    #
    #                         [
    #                             ("select.event", "polygon +ldt"),
    #                             ("select.event", "item +ldt")
    #                         ]
    notifiers = []
)
