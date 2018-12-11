# library importation
# *************************************
# *************************************
import networkx as nx
# for manipulation nodes and edges
import matplotlib.pyplot as plt
# for drawing a simple static graph
import random
# for generating random edge weigh
# *************************************
# *************************************
# renaming and simplifying functions
# for theorical manipulation of graphs
# ************************************
# 1- Creating empty graph
# *******BEGIN***********


def creategraph():
   return nx.Graph()
# *******END*************
# 2- Adding new node, in parameters
# parameters : ***
# 2.1-g : the existing graph
# 2.2-n : the node desired to add
# 2.3-visited : bool variable, initially to 'false'
# *******BEGIN*****************


def addNode(g,n,visited):
   g.add_node(n, label=visited)
# *******END*******************
# 3- Adding new edge, in parameters
# parameters : ***
# 3.1-g : the existing graph
# 3.2-nodea : the node source
# 3.3-nodeb : the node destination
# in fact in an undirected graph, there is no really a source or destination node, a source node is considered
# as destination node and so on
# 3.4-weighValue : The value of the edge
# *******BEGIN*****************


def addEdge(g,nodea,nodeb,weightValue):
    g.add_edge(nodea,nodeb, weight=weightValue)
# *******END***********************************
# 4- Displaying simple static graph
# parameters : ***
# 4.1-g : the existing graph
# *******BEGIN*********************


def drawgraph(g):
    nx.draw(g)
    plt.show()
# *******END***********************
# 5- simplifying test link, test if 2 noeuds are linked or not
# parameters : ***
# 5.1- g : the existing graph
# 5.2- i: the first node
# 5.3- j: the second node


def isLinked(g, i, j):
    return g.has_edge(i, j)
# 6- generate complete graph with random edges weight, returns a graph, calls create graph
# {Definition: complete graph is a graph that each node is connected to all the other nodes, it has
# nbnodes * (nbnodes - 1) /2
# parameters : ***
# 6.1- nbnodes : The number of nodes given as entry
# *******BEGIN*************************************************************************************


def generaterandgraph(nbnodes):
    g = creategraph()
    for i in range(nbnodes):
        addNode(g, i, 'false')
    for i in range(nbnodes):
        for k in range(i+1,nbnodes,1):
            addEdge(g, i, k, random.randint(1, 10))

    return g
# *******END***************************************************************************************
# Initializing current stack
currentStack = []
# Initializing the stack containing the optimal cycle, named minStack
minStack=[]
# adding the total value as first element of the two stacks
currentStack.append(0)
minStack.append(0)
# functions usede for implementing Algorithmes for finding hameltonian cycle
# **************************************************************************************************************
# **************************************************************************************************************
# 1- add2min function, which compares the current stack and the min stack and update min stack if necessary
# parameters : ***
# 1.1- g : the existing graph
# 1.2- list1: the current list
# 1.3- list2: the optimized list (with hameltonian minimum cycle)
# 1.4- dfs_m_resultat: the number ot nodes visited before executing the function, if is used as a test condition
# for extracting complete candidate cycles using a for loop
# 1.5- nbnodes: the existing graph number of nodes, to be compared to dfs_m_resultat
# *******BEGIN**************************************************************************************************


def add2min(g,list1, list2, dfs_m_result, nbnodes):
    if len(list1) == nbnodes+1 and isLinked(g, list1[len(list1)-1], list1[1]):
        list1[0] = list1[0] + g[list1[len(list1)-1]][list1[1]]['weight']
        if len(list2) == 1:
            list2[0] = list1[0]
            for i in range(nbnodes):
                list2.append(list1[i+1])
                print(list2[i], "is the value")
        if 0 < list1[0] < list2[0]:
            for i in range(nbnodes+1):
                list2[i] = list1[i]
# *******END*****************************************************************************************************
# 2- The main algorithme structure, a dfs modified that generates all possible cases and calls add2min the update
# the minimum stack after each test case
# parameters : ***
# 2.1- g : the existing graph
# 2.2- i: the start node, the choise is optional because all the test cases are obtained from any node
# 2.3- l: the current stack to put the visited nodes participating in the path, they are sorted
# 2.4- ll: the min stack representing the instant optimal path obtained from precedent test cases, at the end
# we obtain on it the optimal hameltonian cycle for the graph
# for extracting complete candidate cycles using a for loop
# 2.5- mm: the count of nodes visited, it is used for test and as an access for add2min function
# *******BEGIN**************************************************************************************************


def dfs(g, i, l, ll, mm):
    mm = mm+1
    print("visiting node",i)
    l.append(i)
    for k in range(g.number_of_nodes()):
        if isLinked(g, i, k) and l.count(k) == 0:
            l[0] = l[0]+g[i][k]['weight']
            dfs(g, k, l, ll, mm)
            print("delete last value")
            add2min(g, l, ll, m, g.number_of_nodes())
            l.pop()
            l[0] = l[0]-g[i][k]['weight']
            mm = mm-1
# *******END*****************************************************************************************************
# The equivalent to main program


# Generating graph with 4 nodes as an example
mainGraph = generaterandgraph(4)
# Displaying the graph generated above
drawgraph(mainGraph)
# Initializing the number of visited nodes to 0
m = 0
# Calling the main algorithm
dfs(mainGraph, 0,currentStack,minStack, m)
# Testing the optimal cycle generated by printing the ordered list of nodes and the optimal total weight
for z in range(1, len(minStack)):
    print(z,"**",minStack[z],"the end")







