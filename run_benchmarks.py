#!/usr/bin/env python3
import argparse,random,statistics,csv,os
from _utils import read_edgelist
ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--out');a=ap.parse_args();G=read_edgelist(a.input);nodes=list(G.nodes());lat=[2.0+0.5*len(list(G.neighbors(random.choice(nodes)))) for _ in range(100)];rows=[{'scheme':'demo','metric':'neighbor_lookup_ms','mean':round(statistics.mean(lat),3),'stdev':round(statistics.pstdev(lat),3)}];os.makedirs(os.path.dirname(a.out),exist_ok=True);w=csv.DictWriter(open(a.out,'w',newline=''),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows);print(rows)
