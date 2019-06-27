from tool.shell import shell
from tool.tst import *
xxx

def tst_code_test():
    return open('test/tst_test.py').read() + open('tool/tst.py').read()


def tst_list_test():
    return tst_list()


def tst_find_test():
    return tst_find()


def tst_run_time_test():
    return shell('date')
