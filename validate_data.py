"""
Validation script for Tutorial 1 data and layer setup
This script checks if the data loads correctly and creates the required layers
"""

import anndata
import numpy as np

print("=" * 60)
print("Tutorial 1 Data Validation")
print("=" * 60)

# Try to load the data
DATA_PATH = 'data/train_adata.h5ad'

try:
    print(f"\n1. Loading data from: {DATA_PATH}")
    adata = anndata.read_h5ad(DATA_PATH)
    print(f"   ✓ Successfully loaded: {adata.n_obs} cells × {adata.n_vars} markers")
    
    print(f"\n2. Checking available layers...")
    layers = list(adata.layers.keys())
    print(f"   Available layers: {layers}")
    
    print(f"\n3. Checking for 'exprs' layer...")
    if 'exprs' in adata.layers:
        print(f"   ✓ 'exprs' layer found")
        print(f"   Shape: {adata.layers['exprs'].shape}")
    else:
        print(f"   ✗ 'exprs' layer NOT found!")
        
    print(f"\n4. Checking for 'exprs_arcsinh' layer...")
    if 'exprs_arcsinh' in adata.layers:
        print(f"   ✓ 'exprs_arcsinh' layer already exists")
    else:
        print(f"   ⚠ 'exprs_arcsinh' layer does NOT exist yet")
        print(f"   Creating it now...")
        adata.layers['exprs_arcsinh'] = np.arcsinh(adata.layers['exprs'] / 5)
        print(f"   ✓ Created 'exprs_arcsinh' layer")
        
    print(f"\n5. Verifying cell type annotations...")
    if 'celltypes' in adata.obs.columns:
        n_types = adata.obs['celltypes'].nunique()
        print(f"   ✓ Found {n_types} cell types")
        print(f"   Cell types: {list(adata.obs['celltypes'].unique()[:5])}...")
    else:
        print(f"   ✗ 'celltypes' column not found!")
        
    print(f"\n6. Checking marker names...")
    if 'marker' in adata.var.columns:
        n_markers = len(adata.var['marker'])
        print(f"   ✓ Found {n_markers} markers")
        print(f"   Example markers: {list(adata.var['marker'].values[:5])}")
    else:
        print(f"   ✗ 'marker' column not found!")

    print("\n" + "=" * 60)
    print("✓ Data validation complete!")
    print("=" * 60)
    print("\nRECOMMENDATION:")
    print("If you're seeing KeyError in the notebook, you need to:")
    print("1. In VS Code: Kernel → Restart Kernel")
    print("2. Or: Click 'Restart' in the Jupyter toolbar")
    print("3. Then re-run cells from the beginning")
    print("\nThis ensures the notebook picks up the latest code changes.")
    print("=" * 60)
    
except FileNotFoundError:
    print(f"\n✗ ERROR: Could not find data file at: {DATA_PATH}")
    print("\nPlease download the data from:")
    print("https://drive.google.com/drive/folders/1pLrAb0Hy6kudQ-BHZ1w_afq18Z9eu_RE")
    print("\nAnd place files in the 'data/' folder:")
    print("  - data/train_adata.h5ad")
    print("  - data/test_adata.h5ad")
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
