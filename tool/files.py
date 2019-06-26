from genericpath import getmtime
from glob import glob
from os import remove, getcwd, listdir, mkdir, access, W_OK, walk
from os.path    import isfile, isdir, join, dirname, exists
from sys        import stdin
from subprocess import Popen,PIPE
from json       import loads


# Gather new lines
def accumulate_new_lines(accumulator, f2):
    d = dirname(accumulator)
    if not exists(d):
        print ('Make directory', d)
        mkdir(d)
    a1 = read_file(accumulator)
    a2 = read_file(f2)
    new_items = [a for a in a2 if not a in a1]
    if new_items != []:
        write_file(accumulator, new_items, True)


# Print the count and directory name
def count_files(directory):
    print (len(list_files(directory)), directory)


# Create the directory if needed
def create_directory(path):
    if path=='' or path=='/':
        return
    create_directory(dirname(path))
    if  not exists(path):
        mkdir (path)


# Delete a relative path name
def delete_file(filename):
    remove(filename)


# Run the command as a process and capture stdout & print it
def do_command(cmd, input=None):
    try:
        if input:
            p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE)
            p.stdin.write(input+'\n')
            p.stdin.close()
        else:
            p = Popen(cmd.split(' '), stdout=PIPE) #
            return  p.stdout.read()[:-1]
    except:
        return '<h1>Command Error</h1>'+\
            '<p>An error occurred while trying to execute the command:</p>'+\
            '<p>COMMAND: %s</p>'%cmd +\
            '<p>INPUT: %s</p>'%input


# Remove strange character encodings and convert from utf to ascii
def encode_text(text, encoding='utf-8'):
    text = fix_chars(text)
    return text.decode(encoding).encode('ascii', 'ignore')


# Remove strange character encodings
def fix_chars(text):
    text = text.replace('\xe2\x80\x94', "-")
    text = text.replace('\xe2\x80\x98', "'")
    text = text.replace('\xe2\x80\x99', "'")
    text = text.replace('\xe2\x80\x9c', '"')
    text = text.replace('\xe2\x80\x9d', '"')
    return text


# Run a grep command and capture output
def grep(pattern,file):
    p = Popen(["grep", pattern, file ], stdout=PIPE)
    return p.stdout.read().decode('utf-8')


# Check if this file is writable
def is_writable(path):
    return access(dirname(path), W_OK) and  (not exists(path) or access(path, W_OK))


# Return the files as a list
def list_files(directory):
    return sorted([f for f in listdir(directory) if isfile(join(directory, f)) ])


# Return the files as a list
def list_dirs(directory):
    return sorted([f for f in listdir(directory) if isdir(join(directory, f)) ])


# Absolute path name from a relative path name
def path_name (relative_filename):
    return join(getcwd(), relative_filename)


# Print a flat list
def print_list(lst):
    for f in lst:
        print (f)


# Print a list two levels deep
def print_list2(lst):
    for v in lst:
        for f in v:
            print (f,)
        print ()


# Read the input as lines of text
def read_input():
    text = stdin.read().split('\n')
    return filter(lambda x:len(rstrip(x))>0, text)


# Read JSON from a file
def read_json(filename):
    if exists(filename):
        return loads(open(filename).read())
    return {}


# Read lines from a file and strip off the tailing newline
def read_file(filename):
    if not exists(filename): return [ ]
    f=open(filename)
    results = f.read().split('\n')
    f.close()
    return results


# Return the text from the file
def read_text(f):
    if exists(f):
        return open(f).read()
    return 'No file found, '+f


# Recursive list
def recursive_list(d):
    matches = []
    for root, dirnames, filenames in walk(d):
        for filename in filenames:
            matches.append(join(root, filename).replace(d+'/',''))
    return matches


# Get a file list sorted by time (recent last)
def time_sort_file(d):
    files = filter(isfile, glob(d + "/*"))
    files.sort(key=lambda x: getmtime(x))
    files = map(lambda p:p.replace(d+'/',''), files)
    return files


# Return the text from the file
def write_text(filename, text, append=None):
    create_directory(dirname(filename))
    f=open(filename, 'a' if append else 'w')
    f.write(text)
    f.close()


# Write lines of text to a file
def write_file(filename, lines, append=None):
    write_text(filename, "\n".join(lines)+"\n", append)


