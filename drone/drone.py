import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def getDroneDistance(placeName):
    G = ox.graph_from_place(placeName, network_type='drive')
    G = ox.get_undirected(G)

    degrees = G.degree()
    odd_degree_nodes = [node for node, degree in dict(degrees).items() if degree % 2 != 0]
    G_odd_complete = nx.complete_graph(odd_degree_nodes)
    odd_matching = nx.algorithms.max_weight_matching(G_odd_complete, maxcardinality=True)
    G.add_edges_from(odd_matching)

    def add_weights_to_edges(G):
        for u, v, d in G.edges(data=True):
            if 'length' not in d:
                weight = nx.dijkstra_path_length(G, u, v, weight='length')
                d["length"] = weight
        return G
    add_weights_to_edges(G)

    euler_circuit = list(nx.eulerian_circuit(G, source=next(iter(G))))
    total_distance_km = sum(nx.path_weight(G, (u, v), weight='length') for (u, v) in euler_circuit) / 1000
    print("The total distance in", placeName, "is:", total_distance_km, "km")
    return total_distance_km

d = getDroneDistance("Outremont, Montreal")
d += getDroneDistance("Verdun, Montreal")
d += getDroneDistance("Saint-Leonard, Montreal")
d += getDroneDistance("Riviere-des-prairies-pointe-aux-trembles, Montreal")
d += getDroneDistance("Le Plateau-Mont-Royal, Montreal")
print("The total distance is", d, "km")
