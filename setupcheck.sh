#!/bin/bash

# To check if python3 is installed
check_python() {
    python_version=$(python3 --version 2>&1)
    if [[ $python_version == *"3"* ]]; then
        return 0
    else
        return 1
    fi
}

# To check if venv exists/create venv if not
start_venv() {
    echo "Creating new virtual environment..."
    if python3 -m venv .venv; then
        echo "Virtual environment created successfully."
        source .venv/bin/activate

        echo "Installing required dependencies..."
        if pip3 install -r ./requirements.txt; then
            echo "Dependencies installed successfully."
            return 0 
        else
            echo "Error: Failed to install dependencies."
            return 1
        fi
    else
        echo "Error: Failed to create virtual environment."
        return 1 
    fi
}