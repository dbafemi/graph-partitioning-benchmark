import networkx as nx, csv, os
from collections import defaultdict

def read_edgelist(path):
 G=nx.Graph();
 for line in open(path):
  if line.strip():
   a,b=line.split();G.add_edge(int(a),int(b))
 return G

def write_vertex_partitions(m,out):
 os.makedirs(os.path.dirname(out),exist_ok=True);w=csv.writer(open(out,'w'));w.writerow(['vertex','partition']);[w.writerow([v,p]) for v,p in m.items()]

def write_edge_partitions(m,out):
 os.makedirs(os.path.dirname(out),exist_ok=True);w=csv.writer(open(out,'w'));w.writerow(['u','v','partition']);[w.writerow([u,v,p]) for (u,v),p in m.items()]

def compute_edge_cut(G,m):
 return sum(1 for u,v in G.edges() if m.get(u)!=m.get(v))

def compute_replication_factor(G,ep,k):
 pbv=defaultdict(set)
 for (u,v),p in ep.items():
  pbv[u].add(p);pbv[v].add(p)
 total=sum(len(s) for s in pbv.values());return total/G.number_of_nodes(),pbv
