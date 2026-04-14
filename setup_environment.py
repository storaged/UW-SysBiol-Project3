#!/usr/bin/env python3
"""
Cross-platform setup script for Systems Biology Spatial Proteomics course
Creates virtual environment and installs all required packages
Works on Windows, macOS, and Linux
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def run_command(cmd, shell=False, check=True):
    """Run a command and handle errors"""
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            check=check,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
        print(f"Error message: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is 3.9 or higher"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("\nERROR: Python 3.9 or higher is required!")
        print("Please install Python 3.9+ and try again.")
        print("Download from: https://www.python.org/downloads/")
        return False
    
    print("✓ Python version is compatible")
    return True


def create_virtual_environment(env_name="sysbio_env"):
    """Create a virtual environment"""
    print_header("Creating Virtual Environment")
    
    env_path = Path(env_name)
    
    if env_path.exists():
        print(f"Virtual environment '{env_name}' already exists.")
        response = input("Do you want to recreate it? (y/N): ").strip().lower()
        if response == 'y':
            print(f"Removing existing environment...")
            import shutil
            shutil.rmtree(env_path)
        else:
            print("Using existing environment.")
            return str(env_path)
    
    print(f"Creating virtual environment: {env_name}")
    
    if not run_command([sys.executable, "-m", "venv", env_name]):
        print("\nERROR: Failed to create virtual environment!")
        print("Try installing python3-venv package (Linux) or reinstalling Python.")
        return None
    
    print(f"✓ Virtual environment created at: {env_path.absolute()}")
    return str(env_path)


def get_pip_executable(env_path):
    """Get the path to pip in the virtual environment"""
    system = platform.system()
    
    if system == "Windows":
        pip_path = Path(env_path) / "Scripts" / "pip.exe"
    else:  # Unix-like (macOS, Linux)
        pip_path = Path(env_path) / "bin" / "pip"
    
    return str(pip_path)


def get_python_executable(env_path):
    """Get the path to Python in the virtual environment"""
    system = platform.system()
    
    if system == "Windows":
        python_path = Path(env_path) / "Scripts" / "python.exe"
    else:  # Unix-like (macOS, Linux)
        python_path = Path(env_path) / "bin" / "python"
    
    return str(python_path)


def upgrade_pip(env_path):
    """Upgrade pip to the latest version"""
    print_header("Upgrading pip")
    
    pip_exe = get_pip_executable(env_path)
    
    print("Upgrading pip to latest version...")
    if not run_command([pip_exe, "install", "--upgrade", "pip"]):
        print("WARNING: Failed to upgrade pip, continuing anyway...")
    else:
        print("✓ pip upgraded successfully")
    
    return True


def install_requirements(env_path):
    """Install packages from requirements.txt"""
    print_header("Installing Required Packages")
    
    pip_exe = get_pip_executable(env_path)
    requirements_file = Path("requirements.txt")
    
    if not requirements_file.exists():
        print(f"ERROR: requirements.txt not found in {Path.cwd()}")
        return False
    
    print(f"Installing packages from requirements.txt...")
    print("This may take several minutes...\n")
    
    # Install with progress
    result = subprocess.run(
        [pip_exe, "install", "-r", str(requirements_file)],
        check=False
    )
    
    if result.returncode != 0:
        print("\nERROR: Failed to install some packages!")
        print("You may need to install them manually.")
        return False
    
    print("\n✓ All packages installed successfully")
    return True


def setup_jupyter_kernel(env_path, kernel_name="sysbio_env"):
    """Set up Jupyter kernel for the virtual environment"""
    print_header("Setting Up Jupyter Kernel")
    
    python_exe = get_python_executable(env_path)
    
    print(f"Registering Jupyter kernel: {kernel_name}")
    
    cmd = [
        python_exe, "-m", "ipykernel", "install",
        "--user",
        f"--name={kernel_name}",
        f"--display-name=Systems Biology ({kernel_name})"
    ]
    
    if not run_command(cmd):
        print("WARNING: Failed to register Jupyter kernel.")
        print("You may need to select the kernel manually in VS Code.")
        return False
    
    print(f"✓ Jupyter kernel '{kernel_name}' registered successfully")
    print("\nIn VS Code, you can now select this kernel from the kernel picker.")
    return True


def print_activation_instructions(env_path):
    """Print instructions for activating the environment"""
    print_header("Setup Complete!")
    
    system = platform.system()
    
    print("Your virtual environment is ready to use.\n")
    
    print("=" * 70)
    print("  IMPORTANT: Download the Data Files")
    print("=" * 70)
    print("\nBefore running the tutorials, download the data from:")
    print("https://drive.google.com/drive/folders/1pLrAb0Hy6kudQ-BHZ1w_afq18Z9eu_RE")
    print("\nPlace the files in a 'data/' folder:")
    print("  data/train_adata.h5ad")
    print("  data/test_adata.h5ad\n")
    
    print("=" * 70)
    print("  Activating the Environment")
    print("=" * 70)
    print("\nTo activate the environment:\n")
    
    if system == "Windows":
        print("  Command Prompt:")
        print(f"    {env_path}\\Scripts\\activate.bat\n")
        print("  PowerShell:")
        print(f"    {env_path}\\Scripts\\Activate.ps1\n")
        print("  Note: You may need to run 'Set-ExecutionPolicy RemoteSigned' in PowerShell first\n")
    else:  # Unix-like
        print(f"    source {env_path}/bin/activate\n")
    
    print("To start Jupyter Notebook:")
    print("    jupyter notebook\n")
    
    print("To use in VS Code:")
    print("    1. Open a notebook file (.ipynb)")
    print("    2. Click on the kernel selector (top-right)")
    print("    3. Select 'Systems Biology (sysbio_env)'\n")
    
    print("To deactivate the environment:")
    print("    deactivate\n")
    
    print("=" * 70)


def main():
    """Main setup function"""
    print_header("Systems Biology - Environment Setup")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Create virtual environment
    env_path = create_virtual_environment("sysbio_env")
    if not env_path:
        return 1
    
    # Upgrade pip
    if not upgrade_pip(env_path):
        return 1
    
    # Install requirements
    if not install_requirements(env_path):
        print("\nSetup completed with errors.")
        print("You may need to install some packages manually.")
        return 1
    
    # Setup Jupyter kernel
    setup_jupyter_kernel(env_path, "sysbio_env")
    
    # Print activation instructions
    print_activation_instructions(env_path)
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nSetup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
