# VS Code Python Debugging Setup Guide

## Overview
This guide will walk you through setting up Visual Studio Code for integrated Python debugging, allowing you to set breakpoints, inspect variables, step through code, and debug your Python applications efficiently.

## Prerequisites
- Visual Studio Code installed
- Python installed on your system
- Basic familiarity with VS Code interface

## Step 1: Install Python Extension

1. **Open VS Code**
2. **Install Python Extension:**
   - Click on the Extensions icon in the sidebar (or press `Ctrl+Shift+X`)
   - Search for "Python"
   - Install the official "Python" extension by Microsoft
   - This extension provides IntelliSense, debugging, code formatting, and more

## Step 2: Configure Python Interpreter

1. **Open Command Palette:**
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. **Select Python Interpreter:**
   - Type "Python: Select Interpreter"
   - Choose the appropriate Python interpreter from the list
   - This is usually your system Python or virtual environment Python

## Step 3: Create Launch Configuration

### Method 1: Quick Setup (Recommended for beginners)

1. **Open your Python file**
2. **Start debugging directly:**
   - Press `F5` or go to Run → Start Debugging
   - VS Code will automatically create a basic configuration
   - Select "Python File" when prompted

### Method 2: Manual Configuration (More control)

1. **Create .vscode folder:**
   - In your project root, create a `.vscode` folder if it doesn't exist
2. **Create launch.json:**
   - Inside `.vscode`, create a file named `launch.json`
3. **Add configuration:**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: Current File (Debug Console)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "debugConsole",
            "justMyCode": true
        },
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "main",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: Attach to Process",
            "type": "python",
            "request": "attach",
            "processId": "${command:pickProcess}",
            "justMyCode": true
        }
    ]
}
```

## Step 4: Understanding Configuration Options

### Common Configuration Properties:

| Property | Description | Values |
|----------|-------------|--------|
| `name` | Display name in debug dropdown | Any string |
| `type` | Debugger type | `"python"` |
| `request` | Debug mode | `"launch"` or `"attach"` |
| `program` | File to run | `"${file}"`, `"${workspaceFolder}/main.py"` |
| `console` | Where to show output | `"integratedTerminal"`, `"debugConsole"` |
| `justMyCode` | Debug only your code | `true` or `false` |
| `args` | Command line arguments | Array of strings |
| `cwd` | Working directory | Path string |
| `env` | Environment variables | Object with key-value pairs |

## Step 5: Using the Debugger

### Setting Breakpoints
1. **Click in the gutter** (left of line numbers) to set a breakpoint
2. **Red dot appears** indicating an active breakpoint
3. **Right-click breakpoint** for conditional options:
   - Conditional breakpoint (breaks when condition is true)
   - Log point (logs message without stopping)

### Starting Debug Session
1. **Press F5** or click the play button in the debug panel
2. **Select configuration** from dropdown if multiple exist
3. **Code execution will pause** at first breakpoint

### Debug Controls
- **Continue (F5):** Resume execution
- **Step Over (F10):** Execute next line in current function
- **Step Into (F11):** Step into function calls
- **Step Out (Shift+F11):** Step out of current function
- **Restart (Ctrl+Shift+F5):** Restart debug session
- **Stop (Shift+F5):** Stop debugging

### Debug Panels
1. **Variables:** Shows local and global variables with current values
2. **Watch:** Monitor specific expressions
3. **Call Stack:** Shows function call hierarchy
4. **Breakpoints:** Manage all breakpoints

## Step 6: Advanced Debugging Scenarios

### Debugging with Command Line Arguments
```json
{
    "name": "Python: With Arguments",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "args": ["arg1", "arg2", "--flag"],
    "console": "integratedTerminal"
}
```

### Debugging Web Applications (Flask/Django)
```json
{
    "name": "Python: Flask App",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/app.py",
    "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development"
    },
    "args": ["run", "--debug"],
    "console": "integratedTerminal"
}
```

### Debugging Tests
```json
{
    "name": "Python: Pytest",
    "type": "python",
    "request": "launch",
    "module": "pytest",
    "args": ["${workspaceFolder}/tests"],
    "console": "integratedTerminal"
}
```

## Step 7: Debugging Tips and Best Practices

### Effective Debugging Strategies
1. **Start with print statements** to understand program flow
2. **Use breakpoints strategically** at key decision points
3. **Inspect variables** in the Variables panel
4. **Use the Debug Console** to evaluate expressions
5. **Step through code methodically** rather than running to completion

### Debug Console Usage
- **Evaluate expressions:** Type any Python expression
- **Check variable values:** `print(variable_name)`
- **Modify variables:** `variable_name = new_value`
- **Import modules:** `import math`

### Common Issues and Solutions

#### Issue: Debugger not stopping at breakpoints
- **Solution:** Ensure you're running in debug mode (F5, not Ctrl+F5)
- Check that `justMyCode` is set to `true` if debugging third-party code

#### Issue: Variables not showing values
- **Solution:** Ensure you're in a paused state (hit a breakpoint)
- Check that the variable is in the current scope

#### Issue: Python interpreter not found
- **Solution:** Use Command Palette → "Python: Select Interpreter"
- Verify Python is installed and in your system PATH

## Step 8: Keyboard Shortcuts Reference

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Start/Continue Debugging | F5 | F5 |
| Step Over | F10 | F10 |
| Step Into | F11 | F11 |
| Step Out | Shift+F11 | Shift+F11 |
| Toggle Breakpoint | F9 | F9 |
| Stop Debugging | Shift+F5 | Shift+F5 |
| Restart Debugging | Ctrl+Shift+F5 | Cmd+Shift+F5 |

## Example: Simple Debugging Session

Create a file `debug_example.py`:

```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num  # Set breakpoint here
    return total / len(numbers)

def main():
    data = [1, 2, 3, 4, 5]
    result = calculate_average(data)  # Set breakpoint here
    print(f"Average: {result}")

if __name__ == "__main__":
    main()
```

**Debugging Steps:**
1. Set breakpoints on lines with comments
2. Press F5 to start debugging
3. When paused, inspect `numbers`, `total`, and `num` variables
4. Step through the loop to see how `total` accumulates
5. Continue to the second breakpoint and inspect `result`

## Conclusion

With VS Code's integrated Python debugging, you can:
- Efficiently troubleshoot code issues
- Understand program flow and logic
- Inspect variable states at runtime
- Test different code paths
- Improve code quality through systematic debugging

Practice these techniques with your Python projects to become proficient at debugging. Remember that good debugging skills are essential for every Python developer!

## Additional Resources

- [VS Code Python Debugging Documentation](https://code.visualstudio.com/docs/python/debugging)
- [Python Debugger (pdb) Documentation](https://docs.python.org/3/library/pdb.html)
- [VS Code Python Extension Features](https://code.visualstudio.com/docs/python/python-tutorial)