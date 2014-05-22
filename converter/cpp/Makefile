APPNAME = converter
OBJECTS = cmdline.o converter.o
CC = gcc
CXX = g++
SRCS = converter.cpp \
	cmdline.h \
	cmdline.c
#CFLAGS=-std=c99

all: $(OBJECTS)
	$(CXX) $(CFLAGS) $(OBJECTS) -lpcre -o $(APPNAME)

cmdline.o: cmdline.c
	$(CC) $(CFLAGS) -c $< -o $@

converter.o: converter.cpp
	$(CXX) $(CFLAGS) -c $< -o $@

cmdline.c: cmdline.ggo
	gengetopt --input=cmdline.ggo --include-getopt

clean:
	rm -rf *.o $(APPNAME)

.PHONY: check-syntax

check-syntax:
	$(CXX) $(CFLAGS) -Wall -Wextra -fsyntax-only $(SRCS)
