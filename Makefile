CC=g++
CFLAGS=-lm -Wall -std=c++11

all: pair_search_tool reduced_halo_pair_finder

pair_search_tool:
	$(CC) $(CFLAGS) pair_search.cpp pair_search_functions.cpp -o pair_search.exe

reduced_halo_pair_finder:
	$(CC) $(CFLAGS) reduced_halo_pair_finder.cpp -o reduced_halo_pair_finder.exe

clean:
	rm pair_search.exe reduced_halo_pair_finder.exe
