CC=g++
CFLAGS=-lm -Wall -std=c++11

all: pair_search_tool

pair_search_tool:
	$(CC) $(CFLAGS) pair_search.cpp cartesianCoord.cpp sphericalCoord.cpp pair_search_functions.cpp -o pair_search.exe

clean:
	rm pair_search.exe reduced_halo_pair_finder.exe
