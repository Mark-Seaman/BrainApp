#!/bin/bash
# Linux Shell Contexts

figlet 'Sensei Production Server'

alias h='history 60'
alias gs='git status'
alias co='~/commit'
alias dj='./manage.py'

ls -l

. sensei/env/bin/activate
which python
python --version

