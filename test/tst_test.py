from tool.shell import shell
from tool.tst import tst_list


def tst_list_test():
    return tst_list()


def tst_time_test():
    return shell('date')
