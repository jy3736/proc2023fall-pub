#!/bin/bash

if [ -d "__pycache__" ]; then
    rm -rf __pycache__
fi

python -m compileall *.py

# Source directory
source_dir="./__pycache__"

# Target directory (current directory)
target_dir="."

# Iterate through files in the source directory
for file in "$source_dir"/*.pyc; do
    # Extract the base file name without the directory
    filename=$(basename "$file")

    # Check if the filename matches the pattern "xxx.cpython-38.pyc"
    if [[ "$filename" =~ ^(.+)\.cpython-[0-9]+(\.pyc)$ ]]; then
        # Extract the prefix "xxx" and the suffix ".pyc"
        prefix="${BASH_REMATCH[1]}"
        suffix="${BASH_REMATCH[2]}"

        # Rename and copy the file to the target directory
        new_filename="$prefix$suffix"
        cp "$file" "$target_dir/$new_filename"

        echo "Copied '$file' to '$target_dir/$new_filename'"
    else
        echo "Skipping '$file' (Filename does not match the expected pattern)"
    fi
done

if [ -d "__pycache__" ]; then
    rm -rf __pycache__
fi

