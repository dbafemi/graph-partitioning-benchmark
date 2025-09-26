#!/usr/bin/env python3
import argparse
from collections import defaultdict,Counter
from _utils import read_edgelist,write_edge_partitions,compute_replication_factor
ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--partitions',type=int);ap.add_argument('--outdir');a=ap.parse_args();G=read_edgelist(a.input);deg=dict(G.degree());load=Counter();places=defaultdict(set);eparts={}
for u,v in G.edges():
 best_p=min(range(a.partitions), key=lambda p:(load[p],p))
 eparts[(u,v)]=best_p;load[best_p]+=1;places[u].add(best_p);places[v].add(best_p)
write_edge_partitions(eparts,f"{a.outdir}/edge_partitions.csv");rf,_=compute_replication_factor(G,eparts,a.partitions);print('[ok] HDRF-like replication factor',rf)
