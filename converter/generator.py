#! /usr/bin/env python3

import csv
import os
import re
import pathlib
import string
from jinja2 import Template, Environment

import unicode_characters
import zawgyi_characters

class RuleTemplate(string.Template):
    delimiter = '@'

def get_characters (module):
    characters = [x for x in dir(module) if not x.startswith('__')]
    unirepr = lambda x: getattr(module, x).encode('unicode_escape')
    characters = { x: unirepr(x).decode('utf-8') for x in characters}
    return characters

# Custom filter method
def re_sub(value, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, value)

def hex_encode(value):
    return value.encode('utf8').decode('unicode_escape')

def main():
    cwd_dir = pathlib.Path(__file__).parent
    rules_files = list(cwd_dir.glob('*.rules'))
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]

    context = {}
    uni512zg1_file = cwd_dir.joinpath('uni512zg1.rules')
    zg12uni51_file = cwd_dir.joinpath('zg12uni51.rules')
    zg1detect_file = cwd_dir.joinpath('is_zawgyi.rules')
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

    with zg1detect_file.open('r') as rulesFile:
        rules = rulesFile.readlines()
        rules = map(lambda x: x.strip(), rules)
        rules = map(lambda x: RuleTemplate(x).substitute(**zg1_charcters), rules)
        rules = filter(lambda x: x != "", rules)
        rules = filter(lambda x: not x.startswith("#"), rules)
        is_zgy_rule = "|".join(rules)
        context['is_zawgyi_rule'] = is_zgy_rule

    for child_dir in child_dirs:
        for template_file in child_dir.glob("*.template"):
            print("Generating ", template_file.stem)
            with template_file.open('r') as templateFile, \
                open(os.path.join(child_dir.as_posix(), template_file.stem), 'w') as outputFile:
                template = Template(templateFile.read())
                template.environment.filters['re_sub'] = re_sub
                template.environment.filters['hex_encode'] = hex_encode
                outputFile.write(template.render(**context))

main()
