#! /usr/bin/env python3

import os
import pathlib
from jinja2 import Template
import characters
from characters import *
from collections import namedtuple
import string

def main():
    cwd_dir = pathlib.Path(__file__).parent
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]
    context = {}

    add_characters(context)
    add_categories(context)
    add_syllable_rule(context)

    for child_dir in child_dirs:
        for template_file in child_dir.glob("*.template"):
            print("Generating ", template_file.stem)
            with template_file.open('r') as templateFile, \
                open(os.path.join(child_dir.as_posix(), template_file.stem), 'w') as outputFile:
                template = Template(templateFile.read())
                outputFile.write(template.render(**context))

def add_characters (context):
    C = namedtuple('Character', ['name', 'value'])
    chars = [ C(c, getattr(characters, c)) for c in dir(characters) if not c.startswith("__")]
    context['characters'] = chars

def get_digits():
    return [ chr(x) for x in range(ord(digit_zero), ord(digit_nine)+1)]

def get_consonants():
    return [chr(x) for x in range(ord(letter_ka), ord(letter_a)+1)]

def get_medials():
    return [chr(x) for x in range(ord(medial_ya), ord(medial_ha)+1)]

def get_vowels():
    return [chr(x) for x in range(ord(vowel_tall_aa), ord(vowel_ai)+1)] + [anusvara]

def get_tones():
    return [dot_below, visarga]

def get_diacs():
    return [asat, anusvara] + get_vowels() + get_medials() + get_tones()

def get_puncts():
    return [section, little_section]

def get_indep_vowels():
    return [chr(x) for x in range(ord(letter_i), ord(letter_au)+1)]

def get_symbols():
    return [chr(x) for x in range(ord(symbol_locative), ord(symbol_genitive)+1)]

def add_categories (context):
    categories = []
    C = namedtuple('Category', ['name', 'characters'])
    categories.append(C("digits", get_digits()))
    categories.append(C("consonants", get_consonants()))
    categories.append(C("medials", get_medials()))
    categories.append(C("vowels", get_vowels()))
    categories.append(C("tones", get_tones()))
    categories.append(C("diacs", get_diacs()))
    categories.append(C("puncts", get_puncts()))
    categories.append(C("indep_vowels", get_indep_vowels()))
    categories.append(C("symbols", get_symbols()))
    context['categories'] = categories

def add_syllable_rule (context):
    class RuleTemplate(string.Template): delimiter = '@'

    def get_characters (module):
        _characters = [x for x in dir(module) if not x.startswith('__')]
        unirepr = lambda x: getattr(module, x).encode('unicode_escape')
        _characters = { x: unirepr(x).decode('utf-8') for x in _characters}
        return _characters

    cwd_dir = pathlib.Path(__file__).parent
    syllable_rules = cwd_dir.joinpath('syllable.rules')
    unicharacters = get_characters(characters)
    rules_list = []

    _context = {}
    _context.update(unicharacters)
    _context.update({"digits" : "".join(get_digits())})
    _context.update({"consonants" : "".join(get_consonants())})
    _context.update({"medials" : "".join(get_medials())})
    _context.update({"vowels" : "".join(get_vowels())})
    _context.update({"tones" : "".join(get_tones())})
    _context.update({"diacs" : "".join(get_diacs())})
    _context.update({"puncts" : "".join(get_puncts())})
    _context.update({"indep_vowels" : "".join(get_indep_vowels())})
    _context.update({"symbols" : "".join(get_symbols())})

    with syllable_rules.open('r') as rulesFile:
        for line in rulesFile:
            rule = RuleTemplate(line.strip()).substitute(**_context)
            rules_list.append(rule)

    rule = "|".join(rules_list)
    context.update({'syllable_rule' : rule})

main()
