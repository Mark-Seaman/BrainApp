import traceback
from datetime import datetime
from logging import getLogger
from os.path import join
from json import dumps

from .files import read_text
from sensei.settings import LOG_DIR


def log(text, value=None):
    logger = getLogger(__name__)
    if value:
        text = "%s: %s" % (text,value)
    logger.warning(str(datetime.now())+',  '+text)


def log_exception():
    log('EXCEPTION', traceback.format_exc())


def log_json(text, data):
    log(text, dumps(data, sort_keys=True, indent=4))


def log_file():
    return join(LOG_DIR, 'hammer.log')


def show_log():
    return read_text(log_file())


def log_notifications(title, recipients):
    with open('log/notifications.log', 'a') as f:
        text = "%s, %s, %s" % (str(datetime.now()), title, ' '.join(recipients))
        f.write(text+'\n')


def log_page(request, parms=''):
    message = 'PAGE: url=%s%s, user=%s' % (request.get_host(), request.path, request.user.username)
    if parms:
        message += ', %s' % parms
    log(message)