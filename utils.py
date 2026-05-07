import re

def clean_filename(name):

    name = re.sub(r'[_]', ' ', name)

    return name