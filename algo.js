/* ------- From original script in html ---------- */


// create an array with nodes
var nodes = new vis.DataSet([
		// Uncomment bellow for testing purposes
		// {id: 1, label: "1"},{id: 2, label: "2"},{id: 3, label: "3"},{id: 4, label: "4"}
	]);

// create an array with edges
var edges = new vis.DataSet([
		// Uncomment bellow for testing purposes
		// {from: 1, to: 2},{from: 2, to: 3},{from: 3, to: 4}
	]);

// create a network
var container = document.getElementById('mynetwork');
var containerResultBruteforce = document.getElementById('mynetwork');
var containerResultGreedy = document.getElementById('mynetwork');

var data = {
    nodes: nodes,
    edges: edges
};

var options = {
    interaction:{hover:true},
    manipulation: {
        enabled: true
    }
};

var network = new vis.Network(container, data, options);
var networkResultBruteforce = new vis.Network(containerResultBruteforce, data, options);
var networkResultGreedy = new vis.Network(containerResultGreedy, data, options);

/* ----------------------------------------------- */


this.nbVisitedNodes = 0;
this.adjMat = null;
this.nbNodes = 0;
this.articulationPoints = [];
this.nbArticulationPoints = 0;



/* --------------- Funtions -------------- */






function createAdjMat() {
    var nbNodes = nodes.length;
    var mat = create2DArray(nbNodes);
    var nbEdges;

    for (var i = 0; i < nbNodes; i++) {
        for (var j = 0; j < nbNodes; j++) {
            nbEdges = numberOfEdgesBetweenNodes(i+1, j+1);
            if (nbEdges != 0) nbEdges = 1;
            mat[i][j] = nbEdges;
        }
    }

    return mat;
};



function colorNode(i) {
    var nodeToBeColored = nodes.get(i);

    nodeToBeColored.color = {
        border: '#ffe000',
        background: '#fff000',
        highlight: {
            border: '#ffe000',
            background: '#ffff00'
        },
        hover: {
            border: '#ffe000',
            background: '#ffff00'
        }
    }
    nodes.update(nodeToBeColored);
}


function uncolorAllNodes() {
	for (var i = 0; i < nbNodes; i++) {
		uncolorNode(i+1);
	}
}


function uncolorNode(i) {
    var nodeToBeUncolored = nodes.get(i);

    nodeToBeUncolored.color = {
        border: '#2B7CE9',
        background: '#97C2FC',
        highlight: {
          border: '#2B7CE9',
          background: '#D2E5FF'
        },
        hover: {
          border: '#2B7CE9',
          background: '#D2E5FF'
        }
    }
    nodes.update(nodeToBeUncolored);
}


function DFS(i) {
    var k = 0;
    var temp = -1;

    this.adjMat[0][i] = 2;
    if (i === 0) {
        for (k = 0; k < this.nbNodes; k++) {
            if ((this.adjMat[k][i] === 1) && (k !== i) && this.adjMat[0][k] !== 2) {
                temp = k;
                break;
            }
        }
        ;
        for (k = 0; k < this.nbNodes; k++) {
            if ((this.adjMat[k][i] === 1) && (k !== i) && this.adjMat[0][k] !== 2) {
                this.nbVisitedNodes++;
                this.DFS(k);
            }
        }
        ;
    }
    else {
        for (k = 0; k < this.nbNodes; k++) {
            if ((this.adjMat[i][k] === 1) && (k !== i) && this.adjMat[0][k] !== 2) {
                temp = k;
                break;
            }
        }
        ;
        for (k = 0; k < this.nbNodes; k++) {
            if ((this.adjMat[i][k] === 1) && (k !== i) && this.adjMat[0][k] !== 2) {
                this.nbVisitedNodes++;
                this.DFS(k);
            }
        }
        ;
    }
    return temp;
};


function DFSwithout(i, m) {
    var k = 0;

    this.adjMat[0][i] = 2;
    if (i === 0) {
        for (k = 0; k < this.nbNodes; k++) {
            if ((this.adjMat[k][i] === 1) && (k !== i) && (k !== m) && this.adjMat[0][k] !== 2) {
                this.nbVisitedNodes--;
                this.DFSwithout(k, m);
            }
        }
        ;
    }
    else {
        for (k = 0; k < this.nbNodes; k++) {
            if ((this.adjMat[i][k] === 1) && (k !== i) && (k !== m) && this.adjMat[0][k] !== 2) {
                this.nbVisitedNodes--;
                this.DFSwithout(k, m);
            }
        }
        ;
    }
};



/* ----------------- Helper Functions ----------------*/

function create2DArray(n) {
    arr = [];

    for (var i = 0; i < n; i++) {
        arr[i] = [];
    }

    return arr;
}


function numberOfEdgesBetweenNodes(node1,node2) {
    return edges.get().filter(function (edge) {
        return (edge.from === node1 && edge.to === node2 )|| (edge.from === node2 && edge.to === node1);
    }).length;
};
