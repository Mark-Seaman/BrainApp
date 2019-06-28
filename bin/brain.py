from os import system
from sys import argv

host = 'seamanfamily.org'


# ----------------------------------
# Command Interpreter

def brain_command(options):
    '''Execute all of the brain specific brains'''
    if options:
        cmd = options[0]
        args = options[1:]

        if cmd == 'commit':
            commit(args)
        elif cmd == 'console':
            console(args)
        elif cmd == 'deploy':
            deploy(args)
        elif cmd == 'restart':
            restart()
        elif cmd == 'serve':
            runserver()
        elif cmd == 'status':
            print('xxx')
            system('cd ~/Brain; git status')
        elif cmd == 'web':
            web()
        else:
            print('No brain command found, ' + cmd)
            brain_help()
    else:
        print('No arguments given')
        brain_help()


def brain_help():
    print('''
    usage:  brain cmd [args]

    cmd:
        TODO: tst, docs, curl, index

        commit (comment) - Commit all changes and push

        console - Open a terminal on the Digital Ocean droplet

        deploy - Send code to server 

        restart - Restart the remote web server

        serve - Run the local web server

        status - Show the git status

        web - Browse to the Brain App web page

    ''')


def commit(args):
    comment = ' '.join(args)
    system('cd ~/Brain; git add .; git commit -m "%s"; git pull; git push' % comment)


def console(args, user=None):
    commmand = ' '.join(args)
    print('Remote Command: %s' % commmand)
    if user:
        system ('ssh %s@%s %s' % (user,host,commmand))
    else:
        system ('ssh sensei@%s %s' % (host,commmand))


def deploy(args):
    commit(args)
    console (['./commit SENSEI_AUTO_COMMIT'])
    restart()
    web()


def restart():
    console(['systemctl restart gunicorn'], 'root')


def runserver():
    system('cd ~/Brain && ./manage.py runserver 8004')


def web():
    url = 'http://'+host
    system('open -a "Google Chrome" %s' % url)


if __name__ == '__main__':
    print(brain_command(argv[1:]))
