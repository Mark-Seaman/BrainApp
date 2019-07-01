from django.core.management.base import BaseCommand
from os import system
import traceback

from tool.log import log_exception

host = 'seamanfamily.org'


# ----------------------------------
# Command Interpreter


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            ocean_command(self, options['script'])
        except:
            log_exception()
            self.stdout.write('** tst Exception (%s) **' % ' '.join(options['script']))
            self.stdout.write(traceback.format_exc())


def ocean_command(self, options):
    '''Execute all of the brain specific brains'''
    self.stdout.write('starting ocean command ...')

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
            system('cd ~/Brain; git status')
        elif cmd == 'web':
            web()
        else:
            print('No ocean command found, ' + cmd)
            ocean_help()
    else:
        print('No arguments given')
        ocean_help()
    self.stdout.write('... ending  ocean command')


def ocean_help():
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


def console(args):
    commmand = ' '.join(args)
    print('Remote Command: %s' % commmand)
    system ('ssh sensei@%s %s' % (host,commmand))


def deploy(args):
    commit(args)
    console (['bin/commit SENSEI_AUTO_COMMIT'])
    restart()
    web()


def restart():
    # console(['sudo systemctl restart gunicorn'])
    print('console -- sudo systemctl restart gunicorn')


def runserver():
    system('cd ~/Brain && ./manage.py runserver 8004')


def web():
    url = 'http://'+host
    system('open -a "Firefox" %s' % url)
