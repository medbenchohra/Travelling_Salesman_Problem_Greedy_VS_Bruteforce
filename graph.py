import networkx as nx
import matplotlib.pyplot as plt
import random



def create_graph():
    return nx.Graph()


def draw_graph(g):
    nx.draw(g)
    plt.show()


def generate_random_graph(nb_nodes):
    g = create_graph()
    for i in range(nb_nodes):
        g.add_node(i, size=65)
    for i in range(nb_nodes):
        for k in range(i+1, nb_nodes):
            g.add_edge(i, k, weight=random.randint(1, 10))
    return g


# Initializing current stack
currentStack = []

# Initializing the stack containing the optimal cycle
minStack = []

# adding the total value as first element of the two stacks
currentStack.append(0)
minStack.append(0)


def add_to_min(g,list1, list2, dfs_m_result, nb_nodes):
    if len(list1) == nb_nodes+1 and g.has_edge(list1[len(list1)-1], list1[1]):
        list1[0] = list1[0] + g[list1[len(list1)-1]][list1[1]]['weight']
        if len(list2) == 1:
            list2[0] = list1[0]
            for i in range(nb_nodes):
                list2.append(list1[i+1])
        if 0 < list1[0] < list2[0]:
            for i in range(nb_nodes+1):
                list2[i] = list1[i]


def dfs(g, i, l, ll, mm):
    mm = mm + 1
    l.append(i)
    for k in range(g.number_of_nodes()):
        if g.has_edge(i, k) and l.count(k) == 0:
            l[0] = l[0]+g[i][k]['weight']
            dfs(g, k, l, ll, mm)
            add_to_min(g, l, ll, visited_nodes, g.number_of_nodes())
            l.pop()
            l[0] = l[0]-g[i][k]['weight']
            mm = mm - 1


mainGraph = generate_random_graph(4)
draw_graph(mainGraph)
visited_nodes = 0

dfs(mainGraph, 0, currentStack, minStack, visited_nodes)

print(minStack)







