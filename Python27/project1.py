# Project 1
# Degree distributions for graphs

EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2={0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    # Takes the number of nodes num_nodes
    # and returns a dictionary corresponding
    # to a complete directed graph with the
    # specified number of nodes.
    complete_graph_dict={}
    if num_nodes>0:
        for tail_i in range(0,num_nodes):
            head_set=set([])
            for head_j in range(0,num_nodes):
                if head_j != tail_i:
                    head_set.add(head_j)
            complete_graph_dict[tail_i]=head_set
    return complete_graph_dict

#complete_dict_3=make_complete_graph(3)
#print complete_dict_3
#
#complete_dict_0=make_complete_graph(0)
#print complete_dict_0
#
#complete_dict_1=make_complete_graph(1)
#print complete_dict_1

def compute_in_degrees(digraph):
    # Takes a directed graph digraph
    # (represented as a dictionary) and
    # computes the in-degrees for the
    # nodes in the graph.
    nodes=digraph.keys()
    heads=digraph.values()
    in_degrees_dict={}
    for node_i in nodes:
        count_i=0
        for head_i in heads:
            if node_i in head_i:
                count_i=count_i+1
        in_degrees_dict[node_i]=count_i
    return in_degrees_dict

#print compute_in_degrees(EX_GRAPH2)

def in_degree_distribution(digraph):
    #Takes a directed graph digraph
    # (represented as a dictionary) and
    # computes the unnormalized distribution
    # of the in-degrees of the graph.
    in_degrees_dict=compute_in_degrees(digraph)
    degrees=in_degrees_dict.values()
    in_degree_distribution_dict={}
    for degree_i in degrees:
        if degree_i in in_degree_distribution_dict:
            in_degree_distribution_dict[degree_i]+=1
        elif degree_i not in in_degree_distribution_dict:
            in_degree_distribution_dict[degree_i]=1
    return in_degree_distribution_dict

#print in_degree_distribution(EX_GRAPH2)
#print in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)