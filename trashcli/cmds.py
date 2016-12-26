# Copyright (C) 2007-2011 Andrea Francia Trivolzio(PV) Italy

import sys,os

def restore():
    from trashcli.restore import RestoreCmd
    RestoreCmd(
        stdout  = sys.stdout,
        stderr  = sys.stderr,
        environ = os.environ,
        exit    = sys.exit,
        input   = raw_input
    ).run(sys.argv)

def empty(argv=sys.argv):
    from trashcli.trash import EmptyCmd
    from trashcli.list_mount_points import mount_points
    from datetime import datetime
    from trashcli.trash import FileSystemReader
    from trashcli.trash import FileRemover
    return EmptyCmd(
        out          = sys.stdout,
        err          = sys.stderr,
        environ      = os.environ,
        list_volumes = mount_points,
        now          = datetime.now,
        file_reader  = FileSystemReader(),
        getuid       = os.getuid,
        file_remover  = FileRemover(),
    ).run(*argv)


def list():
    from trashcli.trash import ListCmd
    from trashcli.list_mount_points import mount_points
    ListCmd(
        out          = sys.stdout,
        err          = sys.stderr,
        environ      = os.environ,
        getuid       = os.getuid,
        list_volumes = mount_points,
    ).run(*sys.argv)

