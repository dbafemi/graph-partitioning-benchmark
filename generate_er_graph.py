#!/usr/bin/env python3
import argparse, networkx as nx, os
ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int);ap.add_argument('--p',type=float);ap.add_argument('--out');a=ap.parse_args();G=nx.gnp_random_graph(a.nodes,a.p,seed=42);os.makedirs(os.path.dirname(a.out),exist_ok=True);open(a.out,'w').writelines(f"{u} {v}\n" for u,v in G.edges());print(f"[ok] ER graph: |V|={G.number_of_nodes()}, |E|={G.number_of_edges()}")
