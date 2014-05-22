APPNAME = converter
OBJECTS = cmdline.o converter.o
CC = gcc
SRCS = converter.c \
	cmdline.h \
	cmdline.c
CFLAGS=-std=c99

all: $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -lpcre -o $(APPNAME)

cmdline.o: cmdline.c
	$(CC) $(CFLAGS) -c $< -o $@

converter.o: converter.c
	$(CC) $(CFLAGS) -c $< -o $@

cmdline.c: cmdline.ggo
	gengetopt --input=cmdline.ggo --include-getopt

clean:
	rm -rf *.o $(APPNAME)

.PHONY: check-syntax

check-syntax:
	$(CC) $(CFLAGS) -Wall -Wextra -fsyntax-only $(SRCS)
