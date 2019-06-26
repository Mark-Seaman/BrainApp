from django.core.management.base import BaseCommand
import traceback

from tool.log import log_exception, log
from tool.tst import tst_command


class Command(BaseCommand):
    help = 'Runs scripts in the Django context'

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            cmd = options['script'][0]
            args = options['script'][1:]
            log('SCRIPTOR: %s %s' % (cmd, args))

            if cmd == 'help':
                self.help()

            elif cmd == 'test':
                self.stdout.write('starting test ...')
                tst_command(self, args)
                self.stdout.write('... ending test')

            else:
                self.stdout.write('**Scriptor Error**: unknown command %s' % options['script'])
                self.help()

        except:
            log_exception()
            self.stdout.write('**Scriptor Exception**')
            self.stdout.write('Scriptor Exception (%s %s)' % (cmd,args))
            self.stdout.write(traceback.format_exc())

    def help(self):
        self.stdout.write('''

            usage: manage.py scriptor command

            command:
                help        - show scriptor commands
                test         - perform diff testing
        ''')
