# Reproducibility Guide

This document provides detailed instructions to reproduce the experiments in:  

**Comparative Analysis of Graph Partitioning Strategies for Enhancing Scalability and Performance in Distributed Graph Databases**  
Submitted to *Cluster Computing* (Springer Nature).  

---

## 1. Hardware and Software Environment

### Cluster Hardware (used in full experiments)
- **Nodes**: 16-node HPC cluster
- **CPU**: Dual Intel Xeon Gold 6338 (64 cores @ 2.0 GHz)
- **RAM**: 512 GB DDR4-3200 ECC per node
- **Storage**: Samsung PM1733 NVMe SSD (3.5 GB/s read, 3.2 GB/s write, ~800k IOPS)
- **Network**: Mellanox ConnectX-6 Dx (100 GbE), Spectrum-2 switch, RTT ≈ 2.1 µs

### Software Stack
- **OS**: Ubuntu 22.04 LTS, Linux kernel 5.15.0, glibc 2.35  
- **JVM**: OpenJDK 17.0.7  
- **Python**: 3.10.12  
- **Graph Database**: Prototype system (commit `a91f5c4`) with partitioning modules  
- **Partitioners**:  
  - Metis v5.1.0 (compiled with `-O3 -fopenmp`)  
  - HDRF (EPFL implementation, commit `5e8d3f7`)  
  - Random Vertex / Random Edge (baseline implementations)  
- **Synthetic Generators**: LFR v1.2.3, Barabási–Albert & Erdős–Rényi (NetworkX v2.8.8)  
- **Benchmark Tools**: OLAPBench v0.7 (extended for OLTP/OLAP queries)  
- **Monitoring Tools**: CPU/memory/network collectors per node  

---

## 2. Quick Reproduction (Demo Scale)

To help reviewers and practitioners, this repository includes **small-scale examples** that can be run on a laptop or single server.

### Step 1. Generate a Synthetic Graph
```bash
python datasets/generate_ba_graph.py --nodes 100000 --edges 500000 --out data/ba.edgelist

### Step 2. Apply Partitioning (HDRF Example)
python scripts/partition_with_hdrf.py --input data/ba.edgelist --partitions 16 --out results/hdrf/


### Step 3. Run Benchmarks
bash scripts/run_benchmarks.sh configs/hdrf_params.yaml


### Step 4. Analyze Results
python scripts/analyze_results.py --input results/hdrf/


## 3. Experimental Parameters
Number of partitions: k = 16 (equal to number of cluster nodes)
Metis imbalance tolerance: δ ≤ 3%
HDRF weights: α = 1.0, β = 0.5, γ = 0.1
Concurrency: 128 clients
Repetitions: 10 runs per configuration
Caching: Disabled (to avoid warm-cache bias)

## 4. Statistical Analysis
All reported results are based on:
Descriptive statistics: mean, SD, 95% CI
Inferential tests: One-way ANOVA, Tukey HSD, Kruskal–Wallis (if assumptions violated)
Effect sizes: Partial η², Cohen’s d
Analysis scripts are provided in scripts/analyze_results.py.

## 5. Limitations of this Repository
The full-scale HPC experiments described in the paper require the hardware listed in Section 1 and cannot be reproduced on commodity hardware.
We therefore provide scaled-down synthetic examples for reproducibility.
All configuration parameters are fully documented to enable replication on similar clusters.

## 6. Citation
If you use this repository, please cite:

@article{oloruntoba2025graphpartitioning,
  title={Comparative Analysis of Graph Partitioning Strategies for Enhancing Scalability and Performance in Distributed Graph Databases},
  author={Omolayo, Olasehinde and Oloruntoba, Oluwafemi and Adepoju, Sheriff and Audu, Khadijah},
  journal={Cluster Computing},
  year={2025}
}
