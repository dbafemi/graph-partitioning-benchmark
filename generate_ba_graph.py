#!/usr/bin/env python3
import argparse, networkx as nx, os, math
ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int);ap.add_argument('--edges',type=int);ap.add_argument('--out');a=ap.parse_args();m=max(1,a.edges//max(1,a.nodes-5));G=nx.barabasi_albert_graph(a.nodes,m,seed=42);os.makedirs(os.path.dirname(a.out),exist_ok=True);open(a.out,'w').writelines(f"{u} {v}\n" for u,v in G.edges());print(f"[ok] BA graph: |V|={G.number_of_nodes()}, |E|={G.number_of_edges()}")
