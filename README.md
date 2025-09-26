# Graph Partitioning Benchmark for Distributed Graph Databases

This repository contains configuration files, synthetic dataset generators, and scripts used in the study:

**Comparative Analysis of Graph Partitioning Strategies for Enhancing Scalability and Performance in Distributed Graph Databases**  
Submitted to *Cluster Computing: The Journal of Networks, Software Tools and Applications* (Springer Nature).

---

## 📂 Repository Contents
- **configs/** — Configuration files for partitioning algorithms and cluster parameters  
- **datasets/** — Synthetic graph generation scripts (Barabási–Albert, Erdős–Rényi, LFR)  
- **scripts/** — Scripts for partitioning, benchmarking, and analysis  
- **results/** — Example outputs and plots from small-scale demo runs  
- **docs/** — Reproducibility notes and references  

---

## ⚡ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/dbafemi/graph-partitioning-benchmark.git
   cd graph-partitioning-benchmark

2. **Install dependencies**
pip install -r requirements.txt

3. **Generate a synthetic dataset**

   python datasets/generate_ba_graph.py --nodes 100000 --edges 500000 --out data/ba.edgelist

4. **Run partitioning (HDRF example)**
python scripts/partition_with_hdrf.py --input data/ba.edgelist --partitions 16 --out results/hdrf/

   
5. **Run benchmarks**
   bash scripts/run_benchmarks.sh configs/hdrf_params.yaml

6. **Analyze results**
   
python scripts/analyze_results.py --input results/hdrf/

🧪 **Notes on Reproducibility**

This repo includes small-scale demo datasets and configs so anyone can replicate experiments without HPC access.

Large-scale experiments (16-node cluster, 512 GB RAM per node, 100 GbE network) are described in the paper (Section 3.4, Table 3).

Due to resource limits, raw HPC traces are not released. However, all parameters and generator settings are documented here.

**Citation**

If you use this repository, please cite our paper:

@article{oloruntoba2025graphpartitioning,
  title={Comparative Analysis of Graph Partitioning Strategies for Enhancing Scalability and Performance in Distributed Graph Databases},
  author={Omolayo, Olasehinde and Oloruntoba, Oluwafemi and Adepoju, Sheriff and Audu, Khadijah and Oluwabukola Racheal Tiamiyu and Deborah Olamide Oyeyemi and Usman Ayobami},
  journal={Cluster Computing},
  year={2025}
}


👥 **Authors**

Olasehinde Omolayo — Georgia State University

Oluwafemi Oloruntoba — Lamar University (Corresponding Author)

Sheriff Adepoju — Prairie View A&M University

Khadijah Audu — University of Arkansas 

Oluwabukola Racheal Tiamiyu -Georgia State University

Deborah Olamide Oyeyemi - University of Dalaware

Usman Ayobami - Western Michigan

**Repository Link**

👉 https://github.com/dbafemi/graph-partitioning-benchmark
