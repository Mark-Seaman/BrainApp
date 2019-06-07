from os import listdir
from os.path import exists, isdir, isfile, join
from subprocess import Popen, PIPE
from sys import version_info


# Read document as HTML
def document_html(path):
    return markdown_to_html(read_markdown(path))


# Create a list of documents (doc, title)
def doc_list(path):
    files = list_files(path)
    result = []
    for f in files:
        result.append((document_title(join(path, f)), f))
    return result
    # return [(document_title(join(path,f)),f) for f in list_files(path)]


def doc_redirect(doc):
    path = join('Documents', doc)
    if isdir(path) and exists(join(path, 'Index.md')):
        return '/%s/Index.md' % doc


# Extract the title from the file text
def document_title(doc):
    text = read_markdown(doc)
    return text.split('\n')[0][2:]


# List the file as hyperlinks to documents
def list_files(path):
    files = listdir('Documents/' + path)
    result = []
    for f in files:
        if isdir(join('Documents', path, f)):
            result.append("%s/" % f)
        else:
            if f != '.DS_Store':
                result.append(f)
    return result
    # return ["%s/" % f if isdir(join('Documents',path,f)) else f for f in listdir('Documents/' + path)]


# Convert markdown text to HTML
def markdown_to_html(markdown):
    return shell_pipe('pandoc', markdown)


# Read the specific document
def read_markdown(doc):
    path = join('Documents', doc)
    if exists(path) and isfile(path):
        return open(path).read()
    else:
        return 'No DOCUMENT Found, %s' % doc


# Read the document formatted as HTML
def render_doc(doc):
    path = join('Documents', doc)
    if not exists(path) and exists(path + '.md'):
        doc = doc + '.md'
    return document_html(doc)


# Run an application and connect with input and output
def shell_pipe(command, stdin=''):
    p = Popen(command, stdin=PIPE, stdout=PIPE)
    if version_info.major == 3:
        (out, error) = p.communicate(input=stdin.encode('utf-8'))
        if error:
            return error.decode('utf-8') + out.decode('utf-8')
        return out.decode('utf-8')
    else:
        (out, error) = p.communicate(input=stdin)
        if error:
            return "**stderr**\n" + error + out
        return out


