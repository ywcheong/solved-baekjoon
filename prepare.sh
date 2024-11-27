#!/bin/bash

# Check if correct number of arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <extension> <path>"
    exit 1
fi

# Assign arguments to variables
extension=$1
path=$2

# Set source and destination paths
source_file="template/template.$extension"
destination_file="solve/$path.$extension"

# Check if source file exists
if [ ! -f "$source_file" ]; then
    echo "Error: Template file $source_file does not exist."
    exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$(dirname "$destination_file")"

# Copy the file
cp "$source_file" "$destination_file"

# Check if copy was successful
if [ $? -eq 0 ]; then
    echo "File copied successfully from $source_file to $destination_file"
else
    echo "Error: Failed to copy file."
    exit 1
fi
