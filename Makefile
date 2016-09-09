CC=g++
CFLAGS=-lm -Wall -std=c++11

all: pair_search_tool

pair_search_tool:
	$(CC) $(CFLAGS) pair_search.cpp -o pair_search

clean:
	rm pair_search
