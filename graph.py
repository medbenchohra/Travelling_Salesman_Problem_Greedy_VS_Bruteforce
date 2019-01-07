import networkx as nx
import matplotlib.pyplot as plt
import random as rnd


def create_graph():
    return nx.Graph()


def color_cycle_edges(graph, to_color):
    nb_nodes = len(to_color)

    print(to_color)
    for i in range(nb_nodes - 2):
        graph[to_color[i+1]][to_color[i+2]]['color'] = 'g'
    graph[to_color[1]][to_color[nb_nodes-1]]['color'] = 'g'


def draw_graph(g):
    color_cycle_edges(g, min_cycle)

    pos = nx.circular_layout(g)

    edges_labels = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edges_labels, rotate=False, label_pos=0.2)

    edges_colors = [g[u][v]['color'] for u, v in g.edges]
    nx.draw(g, pos, width=3, node_size=500, node_color='#A0CBE2', edges=g.edges, edge_color=edges_colors, with_labels=True, font_weight='bold')

    plt.show()


def generate_random_graph(nb_nodes):
    g = create_graph()
    for i in range(nb_nodes):
        g.add_node(i)
    for i in range(nb_nodes):
        for k in range(i+1, nb_nodes):
            g.add_edge(i, k, color='#ECEAE1', weight=rnd.randint(1, 10))

    return g


# Initializing current stack
current_cycle = []

# Initializing the stack containing the optimal cycle
min_cycle = []

# Assigning the cost to the first element
current_cycle.append(0)
min_cycle.append(0)

visited_nodes = 0


def add_to_min(g, current_conf, ideal_conf):
    nb_nodes = g.number_of_nodes()
    if len(current_conf) == nb_nodes + 1:
        last_edge_weight = g[current_conf[len(current_conf)-1]][current_conf[1]]['weight']
        if len(ideal_conf) == 1:
            ideal_conf[0] = current_conf[0] + last_edge_weight
            for i in range(nb_nodes):
                ideal_conf.append(current_conf[i + 1])
        # print("current : ", current_cycle)
        if (current_conf[0] + last_edge_weight) < ideal_conf[0]:
            ideal_conf[0] = current_conf[0] + last_edge_weight
            # print("ideal value : ", ideal_conf[0])
            for i in range(nb_nodes):
                ideal_conf[i+1] = current_conf[i+1]
        # print("ideal : ", ideal_conf)


def brute_force(g, i):
    global visited_nodes
    global current_cycle

    visited_nodes = visited_nodes + 1
    current_cycle.append(i)
    for k in range(g.number_of_nodes()):
        if g.has_edge(i, k) and (current_cycle.count(k) == 0 or (current_cycle.count(k) == 1 and current_cycle[0] == k)):
            # print("")
            current_cycle[0] = current_cycle[0]+g[i][k]['weight']
            brute_force(g, k)
            add_to_min(g, current_cycle, min_cycle)
            current_cycle.pop()
            current_cycle[0] = current_cycle[0] - g[i][k]['weight']
            visited_nodes = visited_nodes - 1


# ---------------------------------------------------------------------------------------
# Main Program
# ------------


main_graph = generate_random_graph(6)
brute_force(main_graph, 0)
draw_graph(main_graph)

print("")
print(min_cycle)




# ignore this comment



