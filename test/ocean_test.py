from tool.shell import shell


def ocean_connect_test():
    return shell('python manage.py ocean console git status')