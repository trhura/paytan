#! /usr/bin/env python

import os
import re
import pathlib
from jinja2 import Template

import declaration

mobileinfo = {}
mobileinfo['mobile_code'] = declaration.mobile_code
mobileinfo['country_code'] = declaration.country_code
mobileinfo['oo_no'] = declaration.oo_no
mobileinfo['tele_no'] = declaration.tele_no
mobileinfo['mpt_no'] = declaration.mpt_no


def js_re_sub(value):
    # js regex doesn't support lookbehinds
    return re.sub("\?<=", "", value)


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
                template.environment.filters['js_re_sub'] = js_re_sub
                outputFile.write(template.render(**mobileinfo))


if __name__ == "__main__":
    main()