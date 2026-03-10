# 0-venv
# Python Virtual Environment Tutorial

"""
VIRTUAL ENVIRONMENT TUTORIAL
============================

This script demonstrates key concepts about Python virtual environments.
Run this script to see how virtual environments work in practice.

PREREQUISITES:
1. Create a virtual environment (see 0-venv.md for instructions)
2. Activate the virtual environment
3. Install required packages: pip install requests
4. Run this script

WHAT THIS SCRIPT DEMONSTRATES:
- Checking if you're in a virtual environment
- Working with packages in isolated environments
- Environment-specific functionality
"""

import sys
import os
import subprocess

def check_virtual_environment():
    """Check if we're running in a virtual environment."""
    print("=== Virtual Environment Check ===")

    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

    if in_venv:
        print("✅ Running in a virtual environment!")
        print(f"Virtual environment path: {sys.prefix}")
        print(f"System Python path: {sys.base_prefix}")
    else:
        print("❌ Not running in a virtual environment")
        print("Please activate your virtual environment first!")
        print("See 0-venv.md for instructions")

    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    return in_venv

def demonstrate_package_isolation():
    """Demonstrate package installation in virtual environment."""
    print("\n=== Package Isolation Demo ===")

    try:
        # Try to import a package that should be installed in venv
        import requests
        print("✅ requests package is available in virtual environment")

        # Make a simple API call to demonstrate functionality
        response = requests.get("https://httpbin.org/get", timeout=5)
        if response.status_code == 200:
            print("✅ Successfully made HTTP request using requests")
            print(f"Response status: {response.status_code}")
        else:
            print(f"⚠️  Unexpected response status: {response.status_code}")

    except ImportError:
        print("❌ requests package not found")
        print("Install it with: pip install requests")
        print("Then run this script again")

def show_environment_info():
    """Show detailed environment information."""
    print("\n=== Environment Information ===")

    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path[:3]}...")  # Show first 3 paths

    # Show environment variables related to Python
    python_env_vars = {k: v for k, v in os.environ.items() if 'python' in k.lower() or 'pip' in k.lower()}
    if python_env_vars:
        print("Python-related environment variables:")
        for key, value in python_env_vars.items():
            print(f"  {key}: {value}")
    else:
        print("No Python-specific environment variables found")

def demonstrate_pip_usage():
    """Demonstrate pip commands and package management."""
    print("\n=== Pip and Package Management ===")

    try:
        # Get pip version
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Pip version: {result.stdout.strip()}")
        else:
            print("❌ Could not get pip version")

        # List installed packages (first few)
        result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=freeze'],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            packages = result.stdout.strip().split('\n')[:5]  # Show first 5 packages
            print("Installed packages (first 5):")
            for package in packages:
                if package.strip():
                    print(f"  {package}")
            if len(result.stdout.strip().split('\n')) > 5:
                print("  ... and more")
        else:
            print("❌ Could not list packages")

    except subprocess.TimeoutExpired:
        print("❌ Pip command timed out")
    except FileNotFoundError:
        print("❌ Pip not found")

def create_requirements_demo():
    """Demonstrate requirements.txt creation and usage."""
    print("\n=== Requirements.txt Demo ===")

    requirements_file = "requirements-demo.txt"

    # Create a simple requirements file
    requirements_content = """requests>=2.25.0
numpy>=1.21.0
matplotlib>=3.5.0
"""

    try:
        with open(requirements_file, 'w') as f:
            f.write(requirements_content)
        print(f"✅ Created {requirements_file}")
        print("Contents:")
        print(requirements_content)

        print("To install these packages, run:")
        print(f"pip install -r {requirements_file}")

    except Exception as e:
        print(f"❌ Could not create requirements file: {e}")

def show_project_structure():
    """Show recommended project structure."""
    print("\n=== Recommended Project Structure ===")
    print("""
my_python_project/
├── venv/                    # Virtual environment (never commit)
├── src/                     # Source code
│   ├── __init__.py
│   └── main.py
├── tests/                   # Test files
├── requirements.txt         # Project dependencies
├── README.md               # Documentation
├── .gitignore              # Ignore venv/, __pycache__/, etc.
└── setup.py                # Optional: for packaging
""")

def main():
    """Main tutorial function."""
    print("🐍 Python Virtual Environment Tutorial")
    print("=" * 50)

    # Run all demonstrations
    venv_active = check_virtual_environment()
    demonstrate_package_isolation()
    show_environment_info()
    demonstrate_pip_usage()
    create_requirements_demo()
    show_project_structure()

    print("\n" + "=" * 50)
    if venv_active:
        print("🎉 Tutorial completed successfully!")
        print("You're now ready to work with Python virtual environments.")
    else:
        print("⚠️  Please activate a virtual environment and run this script again.")
        print("See 0-venv.md for detailed instructions.")

    print("\nNext steps:")
    print("1. Explore the 0-venv.md file for platform-specific instructions")
    print("2. Try creating and managing your own virtual environments")
    print("3. Practice installing packages and managing dependencies")

if __name__ == "__main__":
    main()

