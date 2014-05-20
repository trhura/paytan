#! /usr/bin/env python3

import csv
import os
import pathlib
#from jinja2 import Template
import unicode_characters
import zawgyi_characters

def get_characters (module):
    characters = [x for x in dir(module) if not x.startswith('__')]
    unirepr = lambda x: getattr(module, x).encode('unicode_escape')
    characters = [(x, unirepr(x).decode('utf-8'))for x in characters]
    return characters

def main():
    cwd_dir = pathlib.Path(__file__).parent
    uni512zg1_file = cwd_dir.joinpath('uni512zg1.rules.bak')
    zg12uni51_file = cwd_dir.joinpath('zg12uni51.rules.bak')
    uni51_characters = get_characters(unicode_characters)
    zg1_charcters = get_characters(zawgyi_characters)

    with uni512zg1_file.open('r') as rulesFile, \
         uni512zg1_file.with_suffix('.verbose').open('w') as outputFile:
        rules_reader = csv.reader(rulesFile,delimiter='|')
        rules_writer = csv.writer(outputFile, delimiter="|")
        for uni51, zg1 in rules_reader:
            for name, codepoint in uni51_characters:
                uni51 = uni51.lower().replace(codepoint, '@'+name)
            for name, codepoint in zg1_charcters:
                zg1 = zg1.lower().replace(codepoint, '@'+name)
            rules_writer.writerow([uni51, zg1])

    with zg12uni51_file.open('r') as rulesFile, \
         zg12uni51_file.with_suffix('.verbose').open('w') as outputFile:
        rules_reader = csv.reader(rulesFile,delimiter='|')
        rules_writer = csv.writer(outputFile, delimiter="|")
        for zg1, uni51 in rules_reader:
            for name, codepoint in uni51_characters:
                uni51 = uni51.lower().replace(codepoint, '@'+name)
            for name, codepoint in zg1_charcters:
                #print(name, codepoint)
                zg1 = zg1.lower().replace(codepoint, '@'+name)
            rules_writer.writerow([zg1, uni51])

main()
