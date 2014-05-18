## About ##

Not yet another zawgyi<>unicode converter! Using a set of normalized regular expression rules – adapted from Solveware's [parabeik](https://github.com/ngwestar/parabaik) converter –  the `generate.py` script generates zawgyi<>unicode conversion routines for a variety of programming languages.

Currently, the following languages are supported – `python`, `javascript`, `go`. `php`, `ruby` and `java` will probably added soon.

## Usage ##

+ Install `python3`, `jinja2`
```
$ sudo apt-get install python3
$ sudo pip install jinja2
```

+ Run `generate.py`, and source files for each language will be generated in corresponding directory.
```
$./generate.py
Generating  converter.go
Generating  converter.js
Generating  converter.py

```

+ Grab the source file `converter.*` in corresponding directory, and

## Hacking

+ To add support for another language, just add a directory with corresponding `template` filename. See `python`, `javascript`, `go` directories for example.

## License ##

GPLv2
