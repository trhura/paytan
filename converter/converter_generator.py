#! /usr/bin/env python3

import pathlib
import csv

def main():
    cwd_dir = pathlib.Path(__file__).parent
    child_dirs = [d for d in cwd_dir.iterdir() if d.is_dir()]
    rules_files = list(cwd_dir.glob('*.rules'))

    context = {}
    for each_rules_file in rules_files:
        with each_rules_file.open('r') as rules:
            rules_reader = csv.reader(rules,delimiter='|')
            strip_column = lambda l: list(map(lambda i: i.strip(), l))
            rules_list = [strip_column(r) for r in rules_reader]
            context[each_rules_file.stem] = rules_list

    #for child_dir in child_dirs:
        #with

main()
