#!/usr/bin/env python3
import argparse,random
from _utils import read_edgelist,write_vertex_partitions,compute_edge_cut
ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--partitions',type=int);ap.add_argument('--outdir');a=ap.parse_args();G=read_edgelist(a.input);parts={v:random.randrange(a.partitions) for v in G.nodes()};write_vertex_partitions(parts,f"{a.outdir}/vertex_partitions.csv");print('[ok] Random Vertex edge-cut',compute_edge_cut(G,parts))
