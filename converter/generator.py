#! /usr/bin/env python3

import csv
import os
import pathlib
from jinja2 import Template

def main():
    cwd_dir = pathlib.Path(__file__).parent
    rules_files = list(cwd_dir.glob('*.rules'))
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]

    context = {}
    for each_rules_file in rules_files:
        with each_rules_file.open('r') as rules:
            rules_reader = csv.reader(rules,delimiter='|')
            strip_column = lambda l: list(map(lambda i: i.strip(), l))
            rules_list = [strip_column(r) for r in rules_reader]
            context[each_rules_file.stem + '_rules'] = rules_list

    for child_dir in child_dirs:
        for template_file in child_dir.glob("*.template"):
            with template_file.open('r') as templateFile, \
                open(os.path.join(child_dir.as_posix(), template_file.stem), 'w') as outputFile:
                template = Template(templateFile.read())
                outputFile.write(template.render(**context))

main()
