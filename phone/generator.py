#! /usr/bin/env python

import os
import pathlib
from jinja2 import Template

mobileinfo = {}
mobileinfo['mobile_code'] = 'r"(?P<mobile_code>0?9)"'
mobileinfo['country_code'] = 'r"(?P<country_code>\+?95)"'
mobileinfo['ooredoo'] = 'r"(?P<oordeoo>9(7|6|5)\d{7}$)"'
mobileinfo['telenor'] = 'r"(?P<telenor>7(9|8|7|6)\d{7})$"'
mobileinfo[
    'mpt'
] = 'r"(?P<mpt>5\d{6}|4\d{7,8}|2\d{6,8}|3\d{7,8}|6\d{6}|8\d{6}|7\d{7}|9(0|1|9)\d{5,6})$"'


def main():
    cwd_dir = pathlib.Path(__file__).parent
    child_dirs = [x for x in cwd_dir.iterdir() if x.is_dir()]

    for child_dir in child_dirs:
        for template_file in child_dir.glob("*.template"):
            print("Generating ", template_file.stem)
            with template_file.open('r') as templateFile, open(
                os.path.join(child_dir.as_posix(), template_file.stem), 'w'
            ) as outputFile:
                template = Template(templateFile.read())
                # template.environment.filters['re_sub'] = re_sub
                outputFile.write(template.render(**mobileinfo))


if __name__ == "__main__":
    main()