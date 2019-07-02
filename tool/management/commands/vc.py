from django.core.management.base import BaseCommand
from os import chdir, environ, system
from os.path import exists, join
# from sys import argv
import traceback

from tool.log import log, log_exception
from tool.shell import shell_script


# ------------------------------
# Command Interpreter

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            vc_command(self, options['script'])
        except:
            log_exception()
            self.stdout.write('** tst Exception (%s) **' % ' '.join(options['script']))
            self.stdout.write(traceback.format_exc())

def vc_command(self, options):
    if options:
        cmd = options[0]
        args = options[1:]
        chdir(environ['p'])
        if cmd == 'commit':
            vc_commit(args)
        elif cmd == 'diff':
            vc_diff(args)
        elif cmd == 'log':
            vc_log(args)
        elif cmd == 'pull':
            vc_pull()
        elif cmd == 'push':
            vc_push()
        elif cmd == 'status':
            vc_status()
        else:
            vc_help(args)
    else:
        vc_help(options)


def vc_help(args=None):
    print('''
        vc Command

        usage: x vc COMMAND [ARGS]

        COMMAND:

            commit  - update all local changes in git
            diff    - show uncommitted changes
            log     - show the log on the production server
            pull    - pull all changes from repo
            push    - push all changes to repo
            status  - show git status

        ''')


# ------------------------------
# Functions

def git_cmd(cmd):
    # system(cmd)
    print(git_filter(shell_script(cmd)))


def git_filter(text):

    def ok(line):
        filters = [
            'up to date',
            'up-to-date',
            'nothing',
            'no changes',
            'branch master',
            'origin/master',
            'git add',
            'git checkout',
            'publish your local',
            'insertions(+)',
            'ing objects:',
        ]
        for f in filters:
            if f in line:
                return False
        return True

    text = text.split('\n')
    text = [line for line in text if ok(line)]
    return '\n'.join(text)


def vc_commit(args):
    for d in vc_dirs():
        comment = ' '.join(args)
        cmd = 'echo commit %s && cd %s && git add -A . && git commit -m "%s"'
        git_cmd(cmd % (d, d, comment))
    vc_push()


def vc_diff(args):
    for d in vc_dirs():
        cmd = 'echo diff %s && cd %s && git diff --color'
        git_cmd(cmd % (d, d))


def vc_dirs():
    home   = environ['p']
    doc    = join(environ['p'], 'Documents')
    dirs   = [d for d in [home, doc] if exists(d)]
    return dirs


def vc_log(args):
    d = environ['p']
    system('figlet Sensei')
    cmd = 'echo log %s && cd %s && git log --name-only | head -100'
    git_cmd(cmd %(d, d))
    d = join(d, 'Documents')
    system('figlet Documents')
    cmd = 'echo log %s && cd %s && git log --name-only | head -100'
    git_cmd(cmd %(d, d))


def vc_pull():
    for d in vc_dirs():
        cmd = 'echo pull %s && cd %s && git pull'
        git_cmd(cmd % (d, d))


def vc_push():
    for d in vc_dirs():
        cmd = 'echo push %s && cd %s && git pull; git push'
        git_cmd(cmd % (d, d))


def vc_status():
    for d in vc_dirs():
        cmd = 'echo status %s && cd %s && git status'
        git_cmd(cmd % (d, d))
