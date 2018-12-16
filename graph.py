import networkx as nx
import matplotlib.pyplot as plt
import random as rnd


def create_graph():
    return nx.Graph()


def draw_graph(g):
    pos = nx.circular_layout(g)

    edge_labels = dict([((u, v,), d['weight']) for u, v, d in g.edges(data=True)])
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, rotate=False, label_pos=0.25)

    nx.draw(g, pos, with_labels=True, font_weight='bold')

    plt.show()


def generate_random_graph(nb_nodes):
    g = create_graph()
    for i in range(nb_nodes):
        g.add_node(i)
    for i in range(nb_nodes):
        for k in range(i+1, nb_nodes):
            random_weight = rnd.randint(1, 10)
            g.add_edge(i, k, weight=random_weight)
    return g


# Initializing current stack
currentStack = []

# Initializing the stack containing the optimal cycle
minStack = []

# adding the total value as first element of the two stacks
currentStack.append(0)
minStack.append(0)


def add_to_min(g, current_conf, ideal_conf, nb_nodes):
    if len(current_conf) == nb_nodes+1:
        last_edge_weight = g[current_conf[len(current_conf)-1]][current_conf[1]]['weight']
        if len(ideal_conf) == 1:
            ideal_conf[0] = current_conf[0] + last_edge_weight
            for i in range(nb_nodes):
                ideal_conf.append(current_conf[i + 1])
        print("moh fort", currentStack)
        if (current_conf[0] + last_edge_weight) < ideal_conf[0]:
            ideal_conf[0] = current_conf[0] + last_edge_weight
            print("ideal value : ", ideal_conf[0])
            for i in range(nb_nodes):
                ideal_conf[i+1] = current_conf[i+1]
        print("i:", ideal_conf)


def dfs(g, i, l, ll, mm):
    mm = mm + 1
    l.append(i)
    for k in range(g.number_of_nodes()):
        if g.has_edge(i, k) and (l.count(k) == 0 or (l.count(k) == 1 and l[0] == k)):
            print("")
            # print('l(0) : ', l[0], ' - weight : ', g[i][k]['weight'])
            l[0] = l[0]+g[i][k]['weight']
            dfs(g, k, l, ll, mm)
            add_to_min(g, l, ll, g.number_of_nodes())
            l.pop()
            l[0] = l[0] - g[i][k]['weight']
            mm = mm - 1


mainGraph = generate_random_graph(5)
draw_graph(mainGraph)
visited_nodes = 0

dfs(mainGraph, 0, currentStack, minStack, visited_nodes)

print("")
print(minStack)







