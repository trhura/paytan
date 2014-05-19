#! /usr/bin/env python3

import csv
import os
import pathlib
from jinja2 import Template
import characters
from characters import *

from collections import namedtuple

def main():
    cwd_dir = pathlib.Path(__file__).parent
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]
    context = {}

    add_characters(context)
    add_categories(context)

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

def add_categories (context):
    categories = []
    C = namedtuple('Category', ['name', 'characters'])

    digits = C('digits', [ chr(x) for x in range(ord(digit_zero), ord(digit_nine)+1)])
    consonants = C('consonants', [ chr(x) for x in range(ord(letter_ka), ord(letter_a)+1)])
    medials = C('medials', [ chr(x) for x in range(ord(medial_ya), ord(medial_ha)+1)])
    vowels = C('vowels', [ chr(x) for x in range(ord(vowel_tall_aa), ord(vowel_ai)+1)])
    tones = C('tones', [dot_below, visarga])
    diacs = C('diacs', [asat, anusvara] + vowels.characters + medials.characters + tones.characters)
    puncts = C('puncts', [section, little_section])
    indep_vowels = C('indep_vowels', [chr(x) for x in range(ord(letter_i), ord(letter_au)+1)])
    symbols = C('symbols', [chr(x) for x in range(ord(symbol_locative), ord(symbol_genitive)+1)])

    categories.append(digits)
    categories.append(consonants)
    categories.append(medials)
    categories.append(vowels)
    categories.append(tones)
    categories.append(diacs)
    categories.append(puncts)
    categories.append(indep_vowels)
    categories.append(symbols)
    context['categories'] = categories

main()
