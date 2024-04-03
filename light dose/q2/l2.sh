#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Check if the provided directory exists
if [ ! -d "$1" ]; then
    echo "Error: Directory '$1' not found"
    exit 1
fi

# Create the 'Modified' directory if it doesn't exist
modified_dir="$1/Modified"
if [ ! -d "$modified_dir" ]; then
    mkdir "$modified_dir"
fi

# Find all .txt files recursively and copy them to 'Modified' directory with .bak extension
find "$1" -type f -name "*.txt" -exec sh -c '
    for file do
        cp "$file" "$modified_dir/$(basename "$file" .txt).bak"
    done
' sh {} +