// A C++ program to determine whether a graph is bipartite
#include <cstdlib>
#include <iostream>
#include <fstream>

#include "graph.h"
using namespace std;
 
int main(int argc, char* argv[])
{
    if (argc != 4) 
    {
        cerr << "Incorrect nubmer of command line arguments." << endl;
        cerr << "Usage: "<< argv[0] << " <an input file> <integer> <integer>" << endl;
        return EXIT_FAILURE;
    }

    // read data from an input file
    ifstream inf(argv[1]);
    if (!inf.is_open()) 
    {
        // check if the file can be opened
        cerr << "Error: cannot open an input file \"" << argv[1] << "\"." << endl;
        return EXIT_FAILURE;
    }

    int start = atoi( argv[2] );
    int terminus = atoi( argv[3] );

    WGraph g = WGraph( argv[1] );

    g.find_short_path( start, terminus );

    return EXIT_SUCCESS;
}
