CC=g++
CFLAGS=-lm -Wall -std=c++11

all: reduced_halo_pair_finder n_halo_system_finder

n_halo_system_finder:
	$(CC) $(CFLAGS) n_halo_system_finder.cpp -o n_halo_system_finder.exe

reduced_halo_pair_finder:
	$(CC) $(CFLAGS) reduced_halo_pair_finder.cpp -o reduced_halo_pair_finder.exe

clean:
	rm n_halo_system_finder.exe reduced_halo_pair_finder.exe
