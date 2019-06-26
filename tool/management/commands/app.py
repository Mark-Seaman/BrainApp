from django.core.management.base import BaseCommand
import traceback

from bin.app import app_command
from bin.shell import banner
from tool.log import log, log_exception


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):

        try:
            args = options['script']
            # log('SCRIPTOR: app %s' %  args)
            app_command(args)

        except:
            log_exception()
            self.stdout.write(banner('**Scriptor Exception**'))
            self.stdout.write('Scriptor Exception (%s)' % args)
            self.stdout.write(traceback.format_exc())
