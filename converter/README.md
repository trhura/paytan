## About ##

Not yet another zawgyi<>unicode converter! Using a set of normalized regular expression rules – adapted from Solveware's [parabeik](https://github.com/ngwestar/parabaik) converter –  zawgyi<>unicode conversion routines can be generated for a variety of programming languages.

Currently, the following languages are supported –

* Python
* Java
* Javascript
* Go
* Ruby

We'll add more languages, especially, `php` . And you can send us a pull request!

## Usage ##

+ Install `python3`, `jinja2`

For Ubuntu,
```bash
$ sudo apt-get install python3 python3-jinja2
```

+ For OSX,
```bash
$ brew install python3
$ sudo pip3 install jinja2
```

+ Run `generate.py`, and source files for each language will be generated in corresponding directory.
```
$./generate.py
Generating  converter.go
Generating  Converter.java
Generating  converter.js
Generating  converter.py
Generating  converter.rb
```

+ Grab the source file `converter.*` in corresponding directory, and include it in your project. Then, you can use `uni512zg1` and `zg12uni51` routines for encoding conversions.

## Hacking

+ To add support for another language, just add a directory with corresponding `template` file. See `python`, `javascript`, `go` directories for examples.

## License ##
LGPL V3
