from tool.shell import shell


def vc_status_test():
    return shell('python manage.py vc status')

