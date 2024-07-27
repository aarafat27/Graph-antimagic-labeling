# 🚀 Antimagic Labeling of Graphs Using Prime Numbers

## Overview

This repository contains the implementation and research for the paper titled **"Antimagic Labeling of Graphs Using Prime Numbers"** by Arafat Islam and Md. Imtiaz Habib. The project explores the concept of antimagic labeling for various graph types using prime numbers.

![fig_theory_1](https://github.com/user-attachments/assets/3679a9a4-3a32-4eb2-921a-9c1c9aa8a30d)
<p align="center">Figure: Antimagic labeling for perfect binary tree of level l</p>



## 📚 Research Paper

The research paper, **"Antimagic Labeling of Graphs Using Prime Numbers"**, focuses on assigning distinct prime values to the edges of graphs in a way that ensures the cumulative sum of edge labels at each vertex remains unique. The paper proposes a conjecture on antimagic labeling for any graph and proves two theories. The paper is available on arXiv:
### 🌐 Download:
[Antimagic Labeling of Graphs Using Prime Numbers](https://arxiv.org/abs/2403.17969)

## Code Files

### complete_graph.py

This Python script contains the implementation of the algorithms for antimagic labeling of complete graphs using prime numbers. The script includes the following key components:

- **Prime Number Generation**: Functions to generate prime numbers.
- **Graph Construction**: Functions to construct complete graphs.
- **Antimagic Labeling**: Algorithms to label the edges of the graph with distinct prime numbers.

### Complete_antimagic_code.ipynb

This Jupyter Notebook provides a step-by-step explanation and implementation of the antimagic labeling algorithms. It includes:

- **Mathematical Verification**: Detailed proofs and explanations of the antimagic labeling approach.
- **Algorithm Implementation**: Code cells that implement the prime number generation and graph labeling.
- **Visualization**: Visual representations of the labeled graphs to illustrate the antimagic properties.

## Findings and Conjectures

- **Conjecture**: Every graph can be antimagic labeled using prime numbers.
- **Proof of Theory 1**: Specific types of graphs can be antimagic labeled using a unique set of prime numbers.
- **Proof of Theory 2**: Another class of graphs can be antimagic labeled ensuring unique vertex sums.
- **Unique Vertex Sums**: For all tested graphs, each vertex sum of edge labels is unique.
- **Prime Number Utilization**: The algorithm effectively utilizes prime numbers to achieve antimagic labeling.

## Output

The repository includes sample output images of antimagic labeled graphs. These images demonstrate the uniqueness of vertex sums for different graph types.
![fig_6_perfect5](https://github.com/user-attachments/assets/bf0d3a4e-273a-4610-92c3-cee69e837985)
<p align="center">Figure: Antimagic labeling for perfect binary tree of level 5</p>

![Figure_r1](https://github.com/user-attachments/assets/4bf03af6-66cd-4e42-a16f-a6fa18630e4e)
<p align="center">Figure: Antimagic labeling of K5 complete graph</p>

![Figure_1](https://github.com/user-attachments/assets/8462e69c-f779-44ae-a4c9-cdab83858b88)
<p align="center">Figure: Antimagic labeling of K10 complete graph</p>

![fig_9_pyramid](https://github.com/user-attachments/assets/919cd03c-30b5-46f7-b857-c3d325263c4e)
<p align="center">Figure: Antimagic labeling of W7 pyramid graph</p>

<img width="576" alt="Screenshot 2024-07-25 164857" src="https://github.com/user-attachments/assets/5d546d99-837e-4dbf-b931-7a9960fb06f1">

## Contributing

We welcome contributions to enhance this project. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

