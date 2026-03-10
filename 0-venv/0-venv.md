# 0-venv

## Overview

This tutorial covers Python virtual environments (venv) - isolated environments that allow you to manage project-specific dependencies and avoid conflicts between different projects.

## Learning Objectives

- Understand what virtual environments are and why they're important
- Learn how to create, activate, and deactivate virtual environments
- Master package installation within virtual environments
- Learn best practices for virtual environment management

## Why Virtual Environments?

Virtual environments solve these common problems:

- **Dependency conflicts**: Different projects need different versions of the same package
- **System pollution**: Avoid installing packages globally that might break system tools
- **Reproducibility**: Ensure your project works the same way on different machines
- **Organization**: Keep project dependencies separate and manageable

## Windows Setup

### Creating a Virtual Environment

```bash
# Navigate to your project directory
cd my_project

# Create virtual environment (replace 'venv' with your preferred name)
python -m venv venv
```

### Activating a Virtual Environment

```bash
# Activate (Windows Command Prompt)
venv\Scripts\activate

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Your prompt should now show (venv) at the beginning
```

### Deactivating

```bash
deactivate
```

### Installing Packages

```bash
# Install packages
pip install package_name

# Install from requirements file
pip install -r requirements.txt

# Save current environment to requirements file
pip freeze > requirements.txt
```

## macOS Setup

### Creating a Virtual Environment

```bash
# Navigate to your project directory
cd my_project

# Create virtual environment
python3 -m venv venv
```

### Activating a Virtual Environment

```bash
# Activate
source venv/bin/activate

# Your prompt should now show (venv) at the beginning
```

### Deactivating

```bash
deactivate
```

### Installing Packages

```bash
# Install packages
pip install package_name

# Install from requirements file
pip install -r requirements.txt

# Save current environment to requirements file
pip freeze > requirements.txt
```

## Linux Setup

### Creating a Virtual Environment

```bash
# Navigate to your project directory
cd my_project

# Create virtual environment
python3 -m venv venv
```

### Activating a Virtual Environment

```bash
# Activate
source venv/bin/activate

# Your prompt should now show (venv) at the beginning
```

### Deactivating

```bash
deactivate
```

### Installing Packages

```bash
# Install packages
pip install package_name

# Install from requirements file
pip install -r requirements.txt

# Save current environment to requirements file
pip freeze > requirements.txt
```

## Cross-Platform Commands

These commands work the same on Windows, macOS, and Linux:

```bash
# Check which Python you're using
which python  # or where python on Windows

# Check pip version
pip --version

# List installed packages
pip list

# Upgrade pip
pip install --upgrade pip

# Uninstall a package
pip uninstall package_name

# Show package information
pip show package_name
```

## VS Code Integration

### Selecting Python Interpreter

1. Open your project in VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Python: Select Interpreter"
4. Choose the interpreter from your virtual environment

### Automatic Activation

VS Code can automatically activate your virtual environment when you open a project. Add this to your workspace settings:

```json
{
  "python.terminal.activateEnvironment": true
}
```

## Best Practices

### Project Structure

```
my_project/
├── venv/              # Virtual environment (add to .gitignore)
├── src/               # Source code
├── requirements.txt   # Dependencies
├── README.md         # Documentation
└── .gitignore        # Ignore venv/ directory
```

### .gitignore for Virtual Environments

```
# Virtual environments
venv/
env/
ENV/

# Python
__pycache__/
*.pyc
*.pyo
```

### Requirements Files

```bash
# Create requirements.txt with specific versions
pip freeze > requirements.txt

# Install exact versions
pip install -r requirements.txt

# Create requirements.txt for development
pip freeze > requirements-dev.txt
```

### Managing Multiple Environments

```bash
# Create different environments for different purposes
python -m venv venv-dev      # Development
python -m venv venv-prod     # Production testing
python -m venv venv-test     # Testing

# Activate specific environment
source venv-dev/bin/activate  # Linux/Mac
# or
venv-dev\Scripts\activate     # Windows
```

## Troubleshooting

### Common Issues

**"python" command not found**

- Use `python3` instead of `python` on macOS/Linux
- Ensure Python is installed and in your PATH

**Permission denied when creating venv**

- On macOS/Linux, you might need to adjust permissions
- Try: `chmod +x venv/bin/activate`

**Packages not installing**

- Ensure you're in the activated virtual environment
- Check your internet connection
- Try upgrading pip: `pip install --upgrade pip`

**VS Code not recognizing venv**

- Make sure the venv folder is in your workspace
- Try reloading VS Code window
- Check that python.pythonPath is set correctly

## Notes

- Always activate your virtual environment before working on a project
- Never commit your virtual environment to version control
- Use requirements.txt to share project dependencies
- Consider using tools like `pipenv` or `poetry` for more advanced dependency management
- Virtual environments are lightweight and can be deleted/recreated easily
