from os import chdir, environ, system
from os.path import exists, join
from sys import argv

from shell import shell_script


# ------------------------------
# Command Interpreter

def vc_command(options):
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
            vc_pull(args)
        elif cmd == 'push':
            vc_push(args)
        elif cmd == 'status':
            vc_status(args)
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
    system(cmd)
    # print(git_filter(shell_script(cmd)))


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
    vc_push(args)


def vc_diff(args):
    for d in vc_dirs():
        cmd = 'echo diff %s && cd %s && git diff --color'
        git_cmd(cmd % (d, d))


def vc_dirs():
    home   = environ['p']
    angular = join(environ['HOME'], 'Angular')
    doc    = join(environ['p'], 'Documents')
    rest   = join(environ['HOME'], 'Rest')
    unc    = join(environ['HOME'], 'UNC')
    dirs   = [home, doc, unc]
    dirs   = [d for d in dirs if exists(d)]
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


def vc_pull(args):
    for d in vc_dirs():
        cmd = 'echo pull %s && cd %s && git pull'
        git_cmd(cmd % (d, d))


def vc_push(args):
    for d in vc_dirs():
        cmd = 'echo push %s && cd %s && git pull; git push'
        git_cmd(cmd % (d, d))


def vc_status(args):
    for d in vc_dirs():
        cmd = 'echo status %s && cd %s && git status'
        git_cmd(cmd % (d, d))

if __name__ == '__main__':
    vc_command(argv[1:])