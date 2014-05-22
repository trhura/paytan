APPNAME = converter
OBJECTS = converter.o cmdline.o
CC = gcc
SRCS = converter.c \
	cmdline.h \
	cmdline.c

all: $(OBJECTS)
	$(CC) $(OBJECTS) -lpcre -o $(APPNAME)

cmdline.o: cmdline.c
	$(CC) -c $< -o $@

converter.o: converter.c
	$(CC) -c $< -o $@

cmdline.c: cmdline.ggo
	gengetopt --input=cmdline.ggo --include-getopt

clean:
	rm -rf *.o $(APPNAME)

.PHONY: check-syntax

check-syntax:
	$(CC) $(CFLAGS) -Wall -Wextra -fsyntax-only $(SRCS)
