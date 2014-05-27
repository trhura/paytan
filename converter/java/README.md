## Usage ##

You will need argparse4j library to run this Converter. Here is how I run it.

```
../generator.py && javac -cp argparse4j-0.4.3.jar Converter.java && cat ../tests/myanmar_corpus | java -cp .:argparse4j-0.4.3.jar Converter -t zawgyi > corpus_in_zawgyi
```
