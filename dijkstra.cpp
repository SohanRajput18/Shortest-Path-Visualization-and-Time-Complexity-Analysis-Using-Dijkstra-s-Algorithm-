#include <iostream>
#include <fstream>
#include <limits.h>
#define MAX 100

using namespace std;

// Function to find the vertex with the minimum distance value
int minDistance(int dist[], bool sptSet[], int V) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (!sptSet[v] && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}

// Function to save the distances and paths to a CSV file 
void saveSolutionToCSV(int dist[], int V, int parent[], int start) {
    ofstream dist_file("dijkstra_output.csv");
    ofstream path_file("dijkstra_path.csv");
    if (!dist_file.is_open() || !path_file.is_open()) {
        cout << "Error opening file!" << endl;
        return;
    }

    dist_file << "Vertex,Distance from Source\n";
    path_file << "Vertex,Path\n";
    
    for (int i = 0; i < V; i++) {
        dist_file << i << "," << dist[i] << "\n";
        
        path_file << i << ",";
        // Print the path from start to i
        int j = i;
        while (parent[j] != -1) {
            path_file << j << "<-";
            j = parent[j];
        }
        path_file << start << "\n";
    }
    
    dist_file.close();
    path_file.close();
}

// Function that implements Dijkstra's single source shortest path algorithm 
void dijkstra(int graph[MAX][MAX], int V, int src) {
    int dist[V];
    bool sptSet[V];
    int parent[V]; // To store the shortest path tree

    // Initialize distances and sptSet
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = false;
        parent[i] = -1;
    }

    dist[src] = 0;

    // Find the shortest path for all vertices
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet, V);
        sptSet[u] = true;

        // Update the distance value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++)
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
                parent[v] = u;
            }
    }

    saveSolutionToCSV(dist, V, parent, src);
}

int main() {
    int V;
    int graph[MAX][MAX];
    cout << "Enter the number of vertices: ";
    cin >> V;

    cout << "Enter the adjacency matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cin >> graph[i][j];
        }
    }

    int start_vertex;
    cout << "Enter the start vertex: ";
    cin >> start_vertex;

    dijkstra(graph, V, start_vertex);

    cout << "Dijkstra's algorithm complete\n";
    return 0;
}
