from subprocess import Popen, PIPE
from sys import version_info


# Read document as HTML
def document_html(path):
    return markdown_to_html(read_markdown(path))


# Read the specific document
def read_markdown(doc):
    return open('Documents/%s' % doc).read()


# Convert markdown text to HTML
def markdown_to_html(markdown):
    return shell_pipe('pandoc', markdown)


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