from tool.shell import shell
from tool.tst import *


def tst_code_test():
    return open('tool/tst.py').read()


def tst_list_test():
    return tst_list()


def tst_find_test():
    return tst_find()


def tst_run_time_test():
    return shell('date')
