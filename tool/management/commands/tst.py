from django.core.management.base import BaseCommand
import traceback

from tool.log import log_exception
from tool.tst import tst_command


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            tst_command(self, options['script'])
        except:
            log_exception()
            self.stdout.write('** tst Exception (%s) **' % ' '.join(options['script']))
            self.stdout.write(traceback.format_exc())

