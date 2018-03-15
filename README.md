## About ##

Collections of algorithms commonly used in myanmar language processing. Currently, the following algorithms are available.

+ [Encoding Conversion](#encoding-conversion)
+ [Syllable Break](#syllable-break)
+ [Phone Number Validation](#myanmar-phonenumber)

## Encoding Conversion ##

Not yet another zawgyi<>unicode converter! Using a set of normalized regular expression rules – adapted from Solveware's [parabeik](https://github.com/ngwestar/parabaik) converter –  zawgyi<>unicode conversion routines can be generated for a variety of programming languages.

Currently, the following languages are supported – `python`, `javascript`, `go`, `java` and `ruby`. See its [README](converter/README.md) for more details.


## Syllable Break ##

Break text string into syllables. Only `python` version available for now.

## Myanmar Phonenumber ##

This module support Myanmar phone number validation & normalization. For example, it will normalize the phonenumbers, 942xxx, 0942xxx, +95942xxx into 95942xxx. 

Currently support `python` & `javascript`. 
