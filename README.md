# Thesis Code — Computationally exploring higher order spectra of persistent Laplacians

This repo contains the code for my BEng thesis at Imperial College London. Below is a map of the folders and how they connect to the thesis chapters.

---

## `0_Learning/`

Early exploration and learning material.

- **`PELTS/pelts_learning.ipynb`** — working through the PETLS library to understand how to compute persistent Laplacian spectra.
- **`PELTS/cpp/1_PlapSpectra/plapSpectra.cpp`** — a C++ version of the spectra computation from the library internals.
- **`code_daniel/Old_code_daniel.ipynb`** — old code from Daniel Ruiz Cifuentes, that worked on the Persistent Laplacian with Anthea Monod before, used as a starting reference.

## `1_Experiments_fixed_persistence/` → Chapter 5

Fixed persistence numerical experiments on persistent Laplacian spectra.

- **`make_dataset.py`** — generates the dataset: 50 random point clouds (60 points each), Vietoris-Rips filtration up to dimension 2, scale 0.6, 950 filtration windows. Run this first.
- **`statistical_tests.ipynb`** — the experiments and their graphics.

---

## `2_Random_pairs/` → Chapter 6

Experiments with random pairs of simplicial complexes.

- **`random_pairs.ipynb`** — implements Algorithms 1, 2, and 3 from the thesis and give the functions design for working directly with the boundary matrices and filtration list format of a filtration and the call to generate the dataset.
- **`persistent_laplacian_dataset.pkl`** — saved output from those experiments.


---

## External library: PETLS

All experiments use [PETLS](https://github.com/bdjones13/PETLS) (Jones and Wei, 2025) to compute persistent Laplacian spectra. It is not included in this repo. The documentation can be found [here](https://www.benjones-math.com/software/PETLS/index.html). Appendix A of the thesis lists some issues found while using it.
