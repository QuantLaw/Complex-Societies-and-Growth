[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.4070769.svg)](http://dx.doi.org/10.5281/zenodo.4070769)

# Complex Societies and the Growth of the Law

This repository contains the source of the main paper (unlayouted final version submitted to the publisher) and the supplementary information (SI), along with further graphics and Jupyter notebooks to reproduce the results, for the following publication:

Daniel Martin Katz, Corinna Coupette, Janis Beckedorf, and Dirk Hartung, Complex Societies and the Growth of the Law, *Sci. Rep.* **10** (2020), [https://doi.org/10.1038/s41598-020-73623-x](https://doi.org/10.1038/s41598-020-73623-x)

Related Repositories: 
- [Legal Data Preprocessing](https://github.com/QuantLaw/legal-data-preprocessing) ([Publication Release](http://dx.doi.org/10.5281/zenodo.4070773))
- [Legal Data Clustering](https://github.com/QuantLaw/legal-data-clustering) ([Publication Release](http://dx.doi.org/10.5281/zenodo.4070775))

Related Data: [Preprocessed Input Data](http://dx.doi.org/10.5281/zenodo.4070767)

## Setup

1. It is assumed that you have Python 3.7 installed. (Other versions are not tested.)
2. Set up a virtual environment and activate it. (This is not required but recommended.)
3. Install the required packages `pip install -r requirements.txt`.

## Usage

- To explore the notebooks, start `jupyter lab` from the terminal. 
The prefixes of the notebook names suggest an order in which they may be explored (i.e., notebooks prefixed 01-05 first, then notebooks prefixed si_01-si_05).
- To generate the PDFs of the main paper (unlayouted final version submitted to the publisher) and the SI, execute `latexmk -pdf main-scirep` and `latexmk -pdf si-scirep` in the directory `journal_version`. 
