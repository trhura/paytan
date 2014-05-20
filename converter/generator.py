#! /usr/bin/env python3

import csv
import os
import pathlib
import string
from jinja2 import Template

import unicode_characters
import zawgyi_characters

class RuleTemplate(string.Template):
    delimiter = '@'

def get_characters (module):
    characters = [x for x in dir(module) if not x.startswith('__')]
    unirepr = lambda x: getattr(module, x).encode('unicode_escape')
    characters = { x: unirepr(x).decode('utf-8') for x in characters}
    return characters

def main():
    cwd_dir = pathlib.Path(__file__).parent
    rules_files = list(cwd_dir.glob('*.rules'))
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]

    context = {}
    uni512zg1_file = cwd_dir.joinpath('uni512zg1.rules.verbose')
    zg12uni51_file = cwd_dir.joinpath('zg12uni51.rules.verbose')
    uni51_characters = get_characters(unicode_characters)
    zg1_charcters = get_characters(zawgyi_characters)

    with uni512zg1_file.open('r') as rulesFile:
        rules_reader = csv.reader(rulesFile,delimiter='|')
        rules_list = []
        for uni51, zg1 in rules_reader:
            uni51 = RuleTemplate(uni51.strip()).substitute(**uni51_characters)
            zg1 = RuleTemplate(zg1.strip()).substitute(**zg1_charcters)
            rules_list.append([uni51, zg1])
        context['uni512zg1' + '_rules'] = rules_list

    with zg12uni51_file.open('r') as rulesFile:
        rules_reader = csv.reader(rulesFile,delimiter='|')
        rules_list = []
        for zg1, uni51 in rules_reader:
            uni51 = RuleTemplate(uni51.strip()).substitute(**uni51_characters)
            zg1 = RuleTemplate(zg1.strip()).substitute(**zg1_charcters)
            rules_list.append([zg1, uni51])
        context['zg12uni51' + '_rules'] = rules_list

    for child_dir in child_dirs:
        for template_file in child_dir.glob("*.template"):
            print("Generating ", template_file.stem)
            with template_file.open('r') as templateFile, \
                open(os.path.join(child_dir.as_posix(), template_file.stem), 'w') as outputFile:
                template = Template(templateFile.read())
                outputFile.write(template.render(**context))

main()
