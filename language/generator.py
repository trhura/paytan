#! /usr/bin/env python3

import csv
import os
import pathlib
from jinja2 import Template

from collections import namedtuple
Character = namedtuple('Character', ['name', 'value'])

def main():
    cwd_dir = pathlib.Path(__file__).parent
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]
    context = {}

    import characters as _characters
    characters = [ Character(c, getattr(_characters, c)) for c in dir(_characters) if not c.startswith("__")]
    context['characters'] = characters

    for child_dir in child_dirs:
        for template_file in child_dir.glob("*.template"):
            print("Generating ", template_file.stem)
            with template_file.open('r') as templateFile, \
                open(os.path.join(child_dir.as_posix(), template_file.stem), 'w') as outputFile:
                template = Template(templateFile.read())
                outputFile.write(template.render(**context))

main()
