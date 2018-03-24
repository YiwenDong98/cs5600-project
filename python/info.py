from __future__ import with_statement
import gdb

class CKPTCommand (gdb.Command):
    """Info about this program
Gets the info of the program"""

    def __init__ (self):
        super (CKPTCommand, self).__init__ ("ckpt",
                                                       gdb.COMMAND_SUPPORT,
                                                       gdb.COMPLETE_FILENAME,
                                                       True)

    def invoke (self, arg, from_tty):
        print arg
        gdb.execute("help")

CKPTCommand ()
