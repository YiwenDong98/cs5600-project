from __future__ import with_statement
import gdb

class BackStepCommand (gdb.Command):
    """Back step through program
Step to last step of execusion"""

    def __init__ (self):
        super (BackStepCommand, self).__init__ ("ckpt back",
                                                       gdb.COMMAND_SUPPORT,
                                                       gdb.COMPLETE_FILENAME)

    def invoke (self, arg, from_tty):
        print arg
        gdb.execute("help")

BackStepCommand ()
