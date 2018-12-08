import networkx as nx
import plotly as plt


def createGraph():
   return nx.Graph()


def addNode(g,n,visited):
   g.add_node(n, label=visited)
def addEdge(g,nodea,nodeb,weightValue):
    g.add_edge(nodea,nodeb, weight=weightValue)
def drawGraph(g):
    nx.draw(g)
    plt
def isLinked(g,i,j):
    return(g.get_edge_data(i,j))
g=createGraph()
addNode(g,1,'false')
addNode(g,2,'false')
addNode(g,3,'false')
addEdge(g,1,2,3)
addEdge(g,2,3,5)
drawGraph(g)
l=[]
ll=[]
def dfs(i):
    setattr(g[i],'label','true')
    for k in range(g.number_of_nodes()):
        if((isLinked(g,k,i)) & (g[k]['label']=='false')):
            l.__add__(g[k])
            dfs(k)
            break
        elif((isLinked(g,k,i))):





