/*
 Class Graph is a mockup class, thus you must not assume that this is a completed implementation. 
 Please add codes/comments to complete this class and where you think there is a need.
*/

 #include <vector>
 #include <iostream>
 #include <string>
 #include <fstream>
 #include <sstream>
 #include <algorithm>
 #include <queue>
 #include <map>
 #include <math.h>
 #include <stdio.h> 
 #include <utility>
 #include <iomanip>

using namespace std;

class WGraph
{

private:

	class Node 
    {

        friend class WGraph;

    private:
        
        vector< pair< double, Node* > > Node_cons; //change the order of the pairs
        bool visited = 0;
        int Node_id;
        double Node_dis;

    public:

        Node( int i ){

            Node_id = i;

        }

        void prioritized_vector( bool print ){

            if ( print ){

                cout << "Node: " << Node_id << endl;

            }

            sort( Node_cons.begin(), Node_cons.end() );

            if ( print ){

                for ( auto elem: Node_cons ){

                    cout << "\t" << elem.second->Node_id << ": " << elem.first << endl;

                }

            }

        }

    };


private: // the only Member variable in :

vector< Node* > Node_vec;

public:
	
	WGraph( char* filename ) {

		/* open the file and use a string stream to feed the lines 
		 into a Node, first one is the num, all others are its connections */

        ifstream map_file;
        string line;
        string container;
        map_file.open( filename );

        Node* primary_node;
        Node* con_node;
        
        bool new_node_bool = 0;
        bool con_node_bool = 0;

        double weight;

        int new_node_id;
        int con_node_id;
        int count = 0;

        if ( !map_file.is_open() ){

            cout << "File failed to open, the program is gonna quit!" << endl;
            exit( EXIT_FAILURE );

        }

        /* 
            this block will obtain and partially organize the data so that 
            if will be built into a graph
        */

        while( getline( map_file, line ) ){

            istringstream iss ( line );

            while( iss >> container ){

                if( count == 0 ){

                    //Check to see if this node is already in the list
                    //create a new node pointer and add it to Node_vec

                    new_node_id = stoi( container );

                    for( auto elem: Node_vec ){

                        if ( elem->Node_id == new_node_id ){ //Found it!

                            new_node_bool = 1;
                            primary_node = elem;
                            break; 

                        }

                    }

                    if( !new_node_bool ){ //Didn't find it

                        // add primary_node to the Node_vec
                        primary_node = new Node( new_node_id );
                        Node_vec.push_back( primary_node );

                    }

                }

                else if ( count == 1 ){

                    //check to see if this node is in the list, if not make a new one
                    //then add it to Node_vec
                    //store this in a variable so that it can be combined with the 
                    //weight when count == 2 so it can be put into the map of the node

                    con_node_id = stoi( container );

                    for( auto elem: Node_vec ){

                        if ( elem->Node_id == con_node_id ){ //Found it!

                            con_node_bool = 1;
                            con_node = elem;
                            break; 

                        }

                    }

                    if( !con_node_bool ){ //Didn't find it

                        // add con_node to the Node_vec
                        con_node = new Node( con_node_id );
                        Node_vec.push_back( con_node );

                    }

                }

                else if ( count == 2 ){

                    //using the stored variable of the connected node 
                    //and this third variable, put these bad boys into the original 
                    //node's map 



                    weight = stod( container );
                    pair <double, Node*> new_pair ( weight, con_node );
                    primary_node->Node_cons.push_back( new_pair );

                }

                else{

                    cout << "Something is wrong with the lines in the file. Exiting." << endl;
                    cout << "Or the count variable. " << endl;
                    exit( EXIT_FAILURE );

                }

                ++ count;

            }

            //reset variables after each line

            count = 0;
            new_node_bool = 0;
            con_node_bool = 0;

        }

        for ( auto elem: Node_vec ){

            elem->prioritized_vector( 0 );

        }

    }

	~WGraph() { 

        for( auto elem: Node_vec ){

            elem->Node_cons.clear();

        }

        for( auto elem: Node_vec ){

            delete elem;

        }

	}

    void print_wgraph(){

        for ( auto elem: this->Node_vec ){

            cout << elem->Node_id << endl;

            for ( auto pairs: elem->Node_cons ){

                cout << "   " << pairs.second->Node_id << ": " << pairs.first << endl; 

            }

            cout << endl;

        }

    }
    
    void find_short_path( int start, int terminus ){

        double inf = pow(2, 20); // "Infinity"
        double short_path = 0;
        int count = 0;
        bool there_is_a_path = 0;
        bool first_print = 1;
        bool it_exists = 0;

        vector< int > path_vec;
        vector< pair< double, Node *> > traverse_list;
        pair< double, Node * > U;
        Node *starting_node;
        string path;
        string alt_path;

        for( auto elem: this->Node_vec ){

            if ( elem->Node_id == start ){

                starting_node = elem;
                starting_node->Node_dis = 0;

            }

            else{

                elem->Node_dis = inf;

            }

        }

        for( auto start_connections: starting_node->Node_cons ){

            start_connections.second->Node_dis = start_connections.first;
            traverse_list.push_back( start_connections );

        }

        path = to_string( starting_node->Node_id );
        path_vec.push_back( starting_node->Node_id );
        path_vec.push_back( traverse_list[0].second->Node_id );

        sort( traverse_list.begin(), traverse_list.end() );

        while( !traverse_list.empty() ){

            U = traverse_list[0];
            U.second->visited = 1;
            traverse_list.erase( traverse_list.begin() );

            if( U.second->Node_id == terminus ){

                there_is_a_path = 1;

                short_path = U.second->Node_dis;

                path_vec.push_back( U.second->Node_id );

                break;

            }

            else{

                for( auto neighbors: U.second->Node_cons ){

                    if( neighbors.second->Node_dis == inf ){
                     
                        neighbors.second->Node_dis = neighbors.first + U.second->Node_dis;
                    
                    }
                    
                    else{


                        if( (U.second->Node_dis + neighbors.first) < neighbors.second->Node_dis   ){

                            neighbors.second->Node_dis = (U.second->Node_dis + neighbors.first);

                            for ( auto items: path_vec ){

                                if( U.second->Node_id == items ){

                                    it_exists = 1;

                                }

                            }

                            if ( !it_exists ){

                                path_vec.push_back( U.second->Node_id );
                                it_exists = 0;

                            }

                        }

                    }

                    if( !neighbors.second->visited ){

                        traverse_list.push_back( neighbors );

                    }

                }

                sort( traverse_list.begin(), traverse_list.end() );

            }

        }

        for ( auto items: path_vec ){

            if ( count == 0 ){
             
                alt_path = to_string( items );
                ++count;
            
            }

            else{

                alt_path = alt_path + " -> " + to_string( items );

            }
        }

        if ( there_is_a_path ){

            cout << setprecision( 3 );
            cout << showpoint;

            cout << alt_path << "  " << short_path << endl;
        
        }

        else{

            cout << "NO PATH FOUND" << endl;

        }
    }

};


