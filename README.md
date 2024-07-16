# Antimagic Labeling of Graphs Using Prime Numbers

## Overview

This repository contains the implementation and research for the paper titled **"Antimagic Labeling of Graphs Using Prime Numbers"** by Arafat Islam and Md. Imtiaz Habib. The project explores the concept of antimagic labeling for various graph types using prime numbers.

## Research Paper

The research paper, **"Antimagic Labeling of Graphs Using Prime Numbers"**, focuses on assigning distinct prime values to the edges of graphs in a way that ensures the cumulative sum of edge labels at each vertex remains unique. The paper proposes a conjecture on antimagic labeling for any graph and proves two theories. The paper is available on arXiv:

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
![fig_6_perfect5](https://github.com/user-attachments/assets/03b5ec69-a82c-4925-b3bc-6e984f2ad631)


![Antimagic Labeled Graph](images/output1.png)
![Antimagic Labeled Graph](images/output2.png)

## Contributing

We welcome contributions to enhance this project. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank the Department of Computer Science at American International University-Bangladesh (AIUB) for their support and guidance throughout this research.

## Contact

For any queries or feedback, please contact:

- Arafat Islam: 19-39377-1@student.aiub.edu
- Md. Imtiaz Habib: 19-39389-1@student.aiub.edu
