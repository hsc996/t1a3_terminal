#!/bin/bash

# Setup check
source setupcheck.sh

if check_python; then
    if start_venv; then
        echo "Checks have all passed. Starting application.."
        python3 ./modules/main.py
    else
        echo "Error: Failed to set up virtual environment and install dependencies."
        exit 2
    fi
else
    echo "Error: Python 3 is required to run this application. Please install Python 3 and try again."
    exit 1
fi

# pretty table
# python -m pip install -U prettytable

# colored
# pip install colored

# Run app
python3 main.py