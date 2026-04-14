#!/bin/bash

# Setup script for Unix-based systems (macOS, Linux)
# Systems Biology - Spatial Proteomics Course

echo "========================================="
echo "  Systems Biology Environment Setup"
echo "  Platform: Unix/macOS/Linux"
echo "========================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.9 or higher and try again"
    echo "Download from: https://www.python.org/downloads/"
    exit 1
fi

# Run the Python setup script
echo "Running setup script..."
echo ""

python3 setup_environment.py

# Check if setup was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "  Setup completed successfully!"
    echo "========================================="
    echo ""
    echo "Next steps:"
    echo "  1. Activate the environment:"
    echo "     source sysbio_env/bin/activate"
    echo ""
    echo "  2. Start Jupyter Notebook:"
    echo "     jupyter notebook"
    echo ""
else
    echo ""
    echo "========================================="
    echo "  Setup completed with errors"
    echo "========================================="
    echo ""
    echo "Please check the error messages above and try again."
    exit 1
fi
