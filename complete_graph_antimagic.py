import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Take the number of nodes from the user
n = int(input("Enter number of nodes: "))

# Step 2: Calculate the number of edges in an n-complete graph
num_edges = n * (n - 1) // 2

# Step 3: Generate prime numbers starting from 2 as the edge values
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_edges = []
num = 2
while len(prime_edges) < num_edges:
    if is_prime(num):
        prime_edges.append(num)
    num += 1

# Step 4: Make an undirected complete graph of n nodes and label the edges with prime numbers
G = nx.complete_graph(n)
for i, (u, v) in enumerate(G.edges()):
    G[u][v]['label'] = prime_edges[i]

# Step 5: Calculate the node values and store them in a list
nodes_value = []
for i in range(n):
    node_value = 0
    for u, v, data in G.edges(i, data=True):
        node_value += data['label']
    nodes_value.append(node_value)

# Step 6: Print the list of node values and its size
print("List of Node Values:", nodes_value)
print("Size of the List:", len(nodes_value))

# Step 7: Convert the list into a set and print the size of the set
nodes_value_set = set(nodes_value)
print("Size of the Set:", len(nodes_value_set))

# Step 8: Visualize the graph with nodes and edges labeled
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
nx.draw_networkx_labels(G, pos, labels={i: str(nodes_value[i]) for i in range(n)})
plt.show()
