#!/usr/bin/env python3
import argparse,csv,os,pandas as pd
from _utils import read_edgelist,compute_edge_cut,compute_replication_factor
ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--vertex_partitions');ap.add_argument('--edge_partitions');ap.add_argument('--out');a=ap.parse_args();G=read_edgelist(a.input);rows=[]
if a.vertex_partitions and os.path.exists(a.vertex_partitions):
 vmap={int(r['vertex']):int(r['partition']) for r in csv.DictReader(open(a.vertex_partitions))};cut=compute_edge_cut(G,vmap);rows.append({'scheme':'vertex','metric':'edge_cut_ratio','value':cut/max(1,G.number_of_edges())})
if a.edge_partitions and os.path.exists(a.edge_partitions):
 eparts={(int(r['u']),int(r['v'])):int(r['partition']) for r in csv.DictReader(open(a.edge_partitions))};rf,_=compute_replication_factor(G,eparts,a.partitions if hasattr(a,'partitions') else 16);rows.append({'scheme':'edge','metric':'replication_factor','value':rf})
import pandas as pd;df=pd.DataFrame(rows);os.makedirs(os.path.dirname(a.out),exist_ok=True);df.to_csv(a.out,index=False);print(df)
