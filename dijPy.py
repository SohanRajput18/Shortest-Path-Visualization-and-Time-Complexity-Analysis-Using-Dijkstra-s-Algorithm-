import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

# Function to visualize Dijkstra's algorithm output
def visualize_dijkstra_output(distance_file, path_file):
    df_dist = pd.read_csv(distance_file)
    df_path = pd.read_csv(path_file)
    
    # Print the columns to inspect the DataFrame
    print("Columns in distance DataFrame:", df_dist.columns)
    
    # Visualize distances
    plt.figure(figsize=(10, 6))
    plt.bar(df_dist['Vertex'], df_dist['Distance from Source'], color='skyblue')
    plt.xlabel('Vertex')
    plt.ylabel('Distance from Source')
    plt.title("Dijkstra's Algorithm Shortest Path Distances")
    plt.xticks(df_dist['Vertex'])
    plt.grid(True)
    plt.show()
    
    # Print paths
    print("\nShortest Paths:")
    print(df_path)


def generate_graph(V):
    # Generates a random adjacency matrix for a graph with V vertices
    graph = np.random.randint(1, 10, size=(V, V))
    np.fill_diagonal(graph, 0)
    
    # Ensure the graph is symmetric to represent an undirected graph (if needed)
    graph = np.triu(graph) + np.triu(graph, 1).T
    
    return graph

def dijkstra_time_complexity(V):
    times = []
    for v in range(2, V + 1):
        graph = generate_graph(v)
        start_time = time.time()
        
        # Dummy Dijkstra's implementation for time measurement
        dist = [float('inf')] * v
        spt_set = [False] * v
        dist[0] = 0
        
        for _ in range(v):
            min_distance = float('inf')
            min_index = -1
            
            for i in range(v):
                if not spt_set[i] and dist[i] < min_distance:
                    min_distance = dist[i]
                    min_index = i
                    
            u = min_index
            spt_set[u] = True
            
            for i in range(v):
                if graph[u][i] and not spt_set[i] and dist[i] > dist[u] + graph[u][i]:
                    dist[i] = dist[u] + graph[u][i]
                    
        end_time = time.time()
        times.append(end_time - start_time)
    
    return times

def plot_time_complexity(V, times):
    plt.figure(figsize=(10, 6))
    plt.plot(range(2, V + 1), times, marker='o', linestyle='-', color='b')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (seconds)')
    plt.title("Time Complexity of Dijkstra's Algorithm")
    plt.grid(True)
    plt.show()

# Main function
if __name__ == "__main__":
    distance_file = r'C:\Users\samar\OneDrive\Desktop\PROJECTS\c++ Projects\dijkstra_output.csv'
    path_file = r'C:\Users\samar\OneDrive\Desktop\PROJECTS\c++ Projects\dijkstra_path.csv'
    
    # Visualize the results from Dijkstra's algorithm
    visualize_dijkstra_output(distance_file, path_file)
    
    # Analyze and plot time complexity
    V = 50  # Adjust this value as needed
    times = dijkstra_time_complexity(V)
    plot_time_complexity(V, times)
