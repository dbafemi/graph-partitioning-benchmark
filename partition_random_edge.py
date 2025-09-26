#!/usr/bin/env python3
import argparse,random
from _utils import read_edgelist,write_edge_partitions,compute_replication_factor
ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--partitions',type=int);ap.add_argument('--outdir');a=ap.parse_args();G=read_edgelist(a.input);eparts={(u,v):random.randrange(a.partitions) for u,v in G.edges()};write_edge_partitions(eparts,f"{a.outdir}/edge_partitions.csv");rf,_=compute_replication_factor(G,eparts,a.partitions);print('[ok] Random Edge replication factor',rf)
