# Systems Biology: Spatial Proteomics Analysis

**Block 3: IMC Data and Spatial Niches**  
University of Warsaw, Faculty of Mathematics, Informatics and Mechanics  
BSc Bioinformatics, 3rd Year

---

## Overview

This module focuses on analyzing spatial proteomics data using Imaging Mass Cytometry (IMC). You will learn to work with spatial single-cell data, identify cellular neighborhoods, and discover spatial niches in tumor microenvironments.

**Time commitment**: 2 weeks (1.5h lecture + 4.5h tutorials)

---

## Setup Instructions

### 1. Download the Data

Download the training and test datasets from Google Drive:  
**[Download Data Files](https://drive.google.com/drive/folders/1pLrAb0Hy6kudQ-BHZ1w_afq18Z9eu_RE)**

Place the files in a folder called `data/`:
```
UW-SysBiol-Project3/
├── data/
│   ├── train_adata.h5ad
│   └── test_adata.h5ad
```

### 2. Install Python Environment

**Requirements**: Python 3.9 or higher

#### Automated Setup (Recommended)

**macOS/Linux:**
```bash
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

This will create a virtual environment and install all required packages.

#### Manual Setup

```bash
python3 -m venv sysbio_env
source sysbio_env/bin/activate  # Windows: sysbio_env\Scripts\activate
pip install -r requirements.txt
```

### 3. Start Working

**In VS Code:**
1. Open a notebook file (`.ipynb`)
2. Select kernel: "Systems Biology (sysbio_env)"
3. Run cells!

**In Jupyter:**
```bash
source sysbio_env/bin/activate  # Activate environment
jupyter notebook
```

---

## Tutorial Structure

| Tutorial | Topic | Duration |
|----------|-------|----------|
| **Tutorial 1** | AnnData Structure & Exploratory Analysis | 90 min |
| **Tutorial 2** | Spatial Coordinates & Visualization | 60 min |
| **Tutorial 3** | Neighborhood Graphs with Squidpy | 75 min |
| **Tutorial 4** | Cellular Niches with CellCharter | 75 min |

**Total**: ~5 hours of hands-on practice

---

## Learning Objectives

By completing this module, you will:

- Understand AnnData objects for spatial single-cell data
- Perform exploratory analysis of IMC datasets
- Visualize tissue architecture and spatial patterns
- Build and analyze spatial neighborhood graphs
- Apply dimensionality reduction (PCA) to spatial data
- Identify cellular niches using CellCharter
- Interpret computational results biologically

---

## Dataset Information

**Source**: IMMUcan IMC spatial proteomics dataset

- 253,433 cells across 132 tissue images
- 40 protein markers per cell
- 14 annotated cell types
- Spatial coordinates (X, Y positions)
- Cancer patient samples

---

## Key Technologies

- **AnnData**: Standard format for single-cell data
- **Squidpy**: Spatial omics analysis framework
- **CellCharter**: Automated spatial niche detection
- **scikit-learn**: PCA and clustering
- **matplotlib/seaborn**: Visualization

---

## Troubleshooting

**Python version issues:**
```bash
python3 --version  # Should be 3.9 or higher
```

**Package installation fails:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Jupyter kernel not showing:**
```bash
python -m ipykernel install --user --name=sysbio_env
```

**Still having issues?** Ask during tutorial sessions or check the instructor notes in `md-notes/`.

---

## Project Work

The final assignment involves comparing different spatial analysis methods and interpreting results biologically. Details will be provided in Tutorial 4.

---

## Resources

- [AnnData Documentation](https://anndata.readthedocs.io/)
- [Squidpy Documentation](https://squidpy.readthedocs.io/)
- [CellCharter Documentation](https://cellcharter.readthedocs.io/)

---

**Questions?** Contact course instructors during tutorial sessions.

**Course Year**: 2025/2026
