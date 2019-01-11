import networkx as nx
import matplotlib.pyplot as plt
import random as rnd

# Set the number of nodes in the randomly generated graph
nb_nodes = 7


def create_graph():
    return nx.Graph()


def color_cycle_edges(graph, to_color):
    nodes = len(to_color)
    for i in range(nodes - 2):
        graph[to_color[i+1]][to_color[i+2]]['color'] = 'g'
    graph[to_color[1]][to_color[nodes-1]]['color'] = 'g'


def draw_graph(g):
    color_cycle_edges(g, estimated_cycle)

    pos = nx.circular_layout(g)

    edges_labels = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edges_labels, rotate=False, label_pos=0.2)

    edges_colors = [g[u][v]['color'] for u, v in g.edges]
    nx.draw(g, pos, width=3, node_size=500, node_color='#A0CBE2', edges=g.edges, edge_color=edges_colors, with_labels=True, font_weight='bold')

    plt.show()


def generate_random_graph():
    g = create_graph()
    for i in range(nb_nodes):
        g.add_node(i)
    for i in range(nb_nodes):
        for k in range(i+1, nb_nodes):
            g.add_edge(i, k, color='#ECEAE1', weight=rnd.randint(1, 10))

    return g


# Create an empty list with, the first is to store the cost
estimated_cycle = [0]


# Initializing current stack
current_cycle = []

# Initializing the stack containing the optimal cycle
min_cycle = []

# Assigning the cost to the first element
current_cycle.append(0)
min_cycle.append(0)

visited_nodes = 0


def min_adj_cost(g, node):
    adj_weights = []
    neighbors = [n for n in g.neighbors(node)]

    min_cost = -1
    min_cost_node = -1

    for i in neighbors:
        # print(estimated_cycle)
        estimated_cycle[0] = estimated_cycle[0] - 500
        # print("count ", i, " : ", estimated_cycle.count(i))
        if estimated_cycle.count(i) == 0:
            weight = g[node][i]['weight']
            adj_weights.append(weight)
            if min_cost == -1 or weight < min_cost:
                min_cost = weight
                min_cost_node = i

        estimated_cycle[0] = estimated_cycle[0] + 500

    min_cost = min(adj_weights)
    # print("min : ", min_cost)
    # print("adj :", adj_weights)
    # print("min node : ", neighbors[adj_weights.index(min_cost)])

    return min_cost, min_cost_node


def add_to_min(g, current_conf, ideal_conf):
    nbr_nodes = g.number_of_nodes()
    if len(current_conf) == nbr_nodes + 1:
        last_edge_weight = g[current_conf[len(current_conf)-1]][current_conf[1]]['weight']
        if len(ideal_conf) == 1:
            ideal_conf[0] = current_conf[0] + last_edge_weight
            for i in range(nbr_nodes):
                ideal_conf.append(current_conf[i + 1])
        # print("current : ", current_cycle)
        if (current_conf[0] + last_edge_weight) < ideal_conf[0]:
            ideal_conf[0] = current_conf[0] + last_edge_weight
            # print("ideal value : ", ideal_conf[0])
            for i in range(nbr_nodes):
                ideal_conf[i+1] = current_conf[i+1]
        # print("ideal : ", ideal_conf)


def bruteforce(g, i):
    global visited_nodes
    global current_cycle

    visited_nodes = visited_nodes + 1
    current_cycle.append(i)
    for k in range(g.number_of_nodes()):
        if g.has_edge(i, k) and (current_cycle.count(k) == 0 or (current_cycle.count(k) == 1 and current_cycle[0] == k)):
            # print("")
            current_cycle[0] = current_cycle[0]+g[i][k]['weight']
            bruteforce(g, k)
            add_to_min(g, current_cycle, min_cycle)
            current_cycle.pop()
            current_cycle[0] = current_cycle[0] - g[i][k]['weight']
            visited_nodes = visited_nodes - 1


def greedy(g, i):
    # print(min_adj_cost(g, i)[0])
    estimated_cycle.append(i)
    if len(estimated_cycle) == nb_nodes + 1:
        estimated_cycle[0] = estimated_cycle[0] + g[estimated_cycle[1]][i]['weight']
        return
    estimated_cycle[0] = estimated_cycle[0] + min_adj_cost(g, i)[0]
    greedy(g, min_adj_cost(g, i)[1])

# ---------------------------------------------------------------------------------------
# Main Program
# ------------


main_graph = generate_random_graph()
main_graph_bruteforce = main_graph
main_graph_greedy = main_graph

greedy(main_graph_greedy, 0)
bruteforce(main_graph_bruteforce, 0)

draw_graph(main_graph_greedy)
draw_graph(main_graph_bruteforce)

print("")
print("Estimated Cycle", estimated_cycle)
print("Minimum Cycle", min_cycle)





