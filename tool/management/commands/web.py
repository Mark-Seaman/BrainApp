from django.core.management.base import BaseCommand
from os import environ, system
from os.path import  abspath, exists, join
from platform import node
from sys import argv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pages', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            web_command(options['pages'])
        except:
            log_exception()
            self.stdout.write('** tst Exception (%s) **' % ' '.join(options['script']))
            self.stdout.write(traceback.format_exc())


def web_command(args):
    '''Execute all of the web specific webs'''
    if args:
        web(args[0])
    else:
        web('https://markseaman.info')


def web(page):
    '''Open a web page in Google Chrome'''
    url = page
    if not page.startswith('http://') and not page.startswith('https://'):
        if exists(page):
            url = 'file://' + abspath(page)
        else:
            url = 'http://' + page
    print('firefox %s' % url)
    # Use the correct invocation
    if 'iMac' in node() or 'mac' in node():
        # system('open -a "Google Chrome" '+url)
        system('open -a "Firefox" '+url)
    else:
        system('start firefox '+url)

